"""
SearchScout-AI Core Agent MVP
Author: Ahsan | Track: Applied Search Intelligence
Description: Autonomous Search Intelligence Agent that ingests GSC metrics via DuckDB,
enforces zero-leakage data contracts, calculates priority scores, and generates strategic briefs.
"""

import sys
import os
import json
import duckdb
import pandas as pd
import numpy as np

class SearchScoutAgent:
    def __init__(self, data_path="data/raw/content_refresh_anonymized.csv"):
        self.data_path = data_path
        self.con = duckdb.connect(database=':memory:')
        self.init_warehouse()
        
    def init_warehouse(self):
        """Loads data into in-memory DuckDB warehouse table."""
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Warehouse dataset not found at {self.data_path}")
        self.con.execute(f"CREATE TABLE fact_content AS SELECT * FROM read_csv_auto('{self.data_path}')")
        print(f"[SearchScout-AI] Connected to DuckDB warehouse. Table 'fact_content' loaded.")

    def enforce_data_contract(self, df_sample):
        """Guardrail: Verifies zero post-decision feature leakage in input matrix."""
        forbidden_leakage_cols = ['trend_direction', 'trend_pct', 'future_clicks', 'future_impressions']
        detected_leaks = [col for col in forbidden_leakage_cols if col in df_sample.columns]
        
        if detected_leaks:
            raise ValueError(f"[GUARDRAIL BLOCKED] Data Contract Violation! Leaked columns detected: {detected_leaks}")
        print("[Guardrail Passed] Zero post-decision feature leakage detected.")
        return True

    def query_candidate(self, content_id):
        """Queries single content record from DuckDB warehouse."""
        query = f"""
        SELECT 
            content_id, client_id, days_since_last_update, impressions_90d, 
            clicks_90d, ctr, avg_position, word_count, content_type
        FROM fact_content
        WHERE content_id = '{content_id}'
        """
        res = self.con.execute(query).df()
        if res.empty:
            raise ValueError(f"Content ID '{content_id}' not found in warehouse.")
        return res.iloc[0]

    def score_candidate(self, record):
        """Calculates rule-based and ML baseline priority scores."""
        stale = 1 if record['days_since_last_update'] >= 90 else 0
        mid_volume = 1 if (100 <= record['impressions_90d'] <= 10000) else 0
        low_ctr = 1 if record['ctr'] < 0.5 else 0
        
        score = stale * mid_volume * low_ctr * (100 - record['ctr'])
        
        if score > 50:
            action_label = "REFRESH_IMMEDIATELY"
            reason_code = "stale_mid_volume_low_ctr"
        elif score > 0:
            action_label = "REFRESH_PLAN"
            reason_code = "stale_other"
        else:
            action_label = "MONITOR"
            reason_code = "fresh_or_extreme_volume"
            
        return {
            "score": round(float(score), 2),
            "action_label": action_label,
            "reason_code": reason_code
        }

    def generate_refresh_brief(self, record, scoring):
        """Generates 4-part strategic refresh brief with adversarial critique."""
        brief = f"""
# Search Intelligence Brief: {record['content_id']}
**Client:** {record['client_id']} | **Priority:** {scoring['action_label']} | **Score:** {scoring['score']}/100

### Observed Metrics
- **Staleness:** {record['days_since_last_update']} days since last update
- **Impressions (90d):** {record['impressions_90d']:,}
- **Clicks (90d):** {record['clicks_90d']:,}
- **Click-Through Rate (CTR):** {record['ctr']}%
- **Average Position:** {record['avg_position']}
- **Word Count:** {record['word_count']} words ({record['content_type']})

### Strategic Action Plan
1. **Title & Meta Snippet Overhaul:** Address observed CTR deficit ({record['ctr']}%) by aligning snippet wording with search intent.
2. **Content Structure Refresh:** Expand sub-topics and refresh outdated 90-day-old references.
3. **Internal Linking Boost:** Add 3-5 internal links from high-authority client pages.

### Adversarial Critique (Why this could be wrong)
1. **Deep Ranking Deficit:** Position {record['avg_position']} indicates deep ranking. Low CTR is expected at this position; content updates alone will not recover rankings without domain authority.
2. **Intent Shift / SERP Features:** Search engine layout shifts (e.g. AI Overviews) may be suppressing clicks regardless of content freshness.
"""
        return brief

    def validate_non_causal_language(self, text):
        """Guardrail: Ensures non-causal language compliance."""
        forbidden_phrases = ["guarantee", "will double", "will rank #1", "100% boost"]
        for phrase in forbidden_phrases:
            if phrase in text.lower():
                raise ValueError(f"[GUARDRAIL BLOCKED] Forbidden causal phrase detected: '{phrase}'")
        print("[Guardrail Passed] Non-causal decision-support wording validated.")
        return True

    def run_agent_loop(self, content_id):
        """Executes full end-to-end agent loop."""
        print(f"\n=======================================================")
        print(f"[SearchScout-AI] Initiating Audit Loop for '{content_id}'")
        print(f"=======================================================")
        
        # Step 1: Query DuckDB
        record = self.query_candidate(content_id)
        
        # Step 2: Enforce Data Contract (Feature matrix simulation)
        feature_dict = record.to_dict()
        self.enforce_data_contract(pd.DataFrame([feature_dict]))
        
        # Step 3: Score Candidate
        scoring = self.score_candidate(record)
        
        # Step 4: Generate Brief
        brief = self.generate_refresh_brief(record, scoring)
        
        # Step 5: Validate Language Guardrails
        self.validate_non_causal_language(brief)
        
        print("\n[SearchScout-AI] Loop Completed Successfully. Generated Output:\n")
        print(brief)
        return brief

if __name__ == "__main__":
    agent = SearchScoutAgent()
    # Execute run on real candidate record
    agent.run_agent_loop("content_17c2778a02a9")
