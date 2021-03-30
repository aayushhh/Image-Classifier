#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 12:34:50 2020

@author: Aayush
"""

import pandas as pd
        

main_dir = "../production_data/nov_dec_week4/"
csv_date = "05_dec"

df = pd.read_csv(main_dir + csv_date + "/" + csv_date + ".csv")

final_cust_columns = ["xcall_id", "ORN", "Total no.of attempts(Passed/Failed)", "Store_id", "curated_time",
                      "Response_Date_Time", "Agent_ID", "sigmoid_score", "sigmoid_agg_score",
                      "Output_Type(TP/FP/TN/FN)", "response_code", "fakeface", "is_live", "fake_type"]

final_agent_columns = ["xcall_id", "ORN", "Total no.of attempts(Passed/Failed)", "Store_id", "curated_time",
                      "Response_Date_Time", "Agent_ID", "FIOP_Score", "Output_Type(TP/FP/TN/FN)",
                      "response_code", "fakeface", "is_live", "fake_type"]


total_fp_c = df[(df['sigmoid_score'] > 0) & (df['sigmoid_agg_score'] > 0) & (df['fakeface'] == True) & (df["type"] == 0)]
total_fn_c = df[(df['sigmoid_score'] < 0) & (df['sigmoid_agg_score'] < 0) & (df['fakeface'] == False) & (df["type"] == 0)]

total_fp_a = df[(df['fiopmean'] > 0.25) & (df['fakeface'] == True) & (df["type"] == 1)]
total_fn_a = df[(df['fiopmean'] < 0.25) & (df['fakeface'] == False) & (df["type"] == 1)]


total_fp_c["Output_Type(TP/FP/TN/FN)"] = "FP"
total_fn_c["Output_Type(TP/FP/TN/FN)"] = "FN"

total_fp_a["Output_Type(TP/FP/TN/FN)"] = "FP"
total_fn_a["Output_Type(TP/FP/TN/FN)"] = "FN"


cust_df = pd.concat([total_fp_c, total_fn_c], axis=0)
cust_df["Total no.of attempts(Passed/Failed)"] = " "
cust_df["ORN"] = cust_df["orn"]
cust_df["Store_id"] = cust_df["storeid"]
cust_df["Response_Date_Time"] = pd.to_datetime(cust_df["created_at"]) + pd.DateOffset(hours = 5, minutes = 30)
cust_df["Agent_ID"] = " "
cust_df["fake_type"] = " "
cust_df["curated_time"] = pd.to_datetime(cust_df["curated_time"])

# cust_df["Response_Date_Time"] = ""
# cust_df["Store_id"] = ""
# cust_df["ORN"] = ""


agent_df = pd.concat([total_fp_a, total_fn_a], axis=0)
agent_df["Total no.of attempts(Passed/Failed)"] = " "
agent_df["ORN"] = agent_df["orn"]
agent_df["Store_id"] = agent_df["storeid"]
agent_df["Response_Date_Time"] = pd.to_datetime(agent_df["created_at"]) + pd.DateOffset(hours = 5, minutes = 30)
agent_df["Agent_ID"] = " "
agent_df["FIOP_Score"] = agent_df["fiopmean"]
agent_df["fake_type"] = " "
agent_df["curated_time"] = pd.to_datetime(agent_df["curated_time"])

# agent_df["Response_Date_Time"] = ""
# agent_df["Store_id"] = ""
# agent_df["ORN"] = ""



new_cust_df = cust_df[final_cust_columns]
new_cust_df.to_csv(main_dir + csv_date + "/" + csv_date + "_customer.csv", index=False)

new_agent_df = agent_df[final_agent_columns]
new_agent_df.to_csv(main_dir + csv_date + "/" + csv_date + "_agent.csv", index=False)





