import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Set page config
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# --- Data Generation ---
def generate_mock_data1():
    np.random.seed(42)
    dates = pd.date_range(start='2024-01-01', periods=90, freq='D')
    salespeople = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
    regions = ['North', 'South', 'East', 'West']
    stages = ['Prospecting', 'First Contact', 'Qualified Leads', 'Demo', 'Closed Won', 'Closed Lost']
    companies = ["Company A", "Company B", "Company C", "Company D", "Company E"]
    data = []
    probabilities = [0.2, 0.2, 0.2, 0.2, 0.1, 0.1]
    for date in dates:
        for salesperson in salespeople:
            data.append({
                'Date': date,
                'Salesperson': salesperson,
                'Region': np.random.choice(regions),
                'Revenue': np.random.randint(1000, 10000),
                'Deals Closed': np.random.randint(0, 5),
                'Pipeline Stage': np.random.choice(stages, p=probabilities),
                'First Contact Made': np.random.randint(1, 20),
                'Company': np.random.choice(companies),
                'Opportunity Value': np.random.randint(5000, 50000),
                'Orders Placed': np.random.randint(0, 5),
                'Invoices Issued': np.random.randint(0, 5)
            })
    return pd.DataFrame(data)

def generate_competition_data(num_days=30, salespeople=None):
    if salespeople is None:
        salespeople = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
    dates = pd.date_range(end=pd.Timestamp.now(), periods=num_days)
    data = []
    for date in dates:
        for salesperson in salespeople:
            sales = np.random.randint(0, 10)
            revenue = np.random.randint(1000, 10000) * sales
            leads = np.random.randint(0, 5)
            customer_reviews = np.random.randint(0, 3)
            data.append({
                "Date": date,
                "Salesperson": salesperson,
                "Sales": sales,
                "Revenue": revenue,
                "Leads": leads,
                "Customer Reviews": customer_reviews
            })
    return pd.DataFrame(data)

def generate_activity_data(num_days=30, salespeople=None):
    if salespeople is None:
        salespeople = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
    dates = pd.date_range(end=pd.Timestamp.now(), periods=num_days)
    data = []
    for date in dates:
        for salesperson in salespeople:
            calls = np.random.randint(5, 20)
            emails = np.random.randint(10, 30)
            demos = np.random.randint(0, 3)
            social_interactions = np.random.randint(2, 15)
            data.append({
                "Date": date,
                "Salesperson": salesperson,
                "Calls": calls,
                "Emails": emails,
                "Demos": demos,
                "Social Interactions": social_interactions,
            })
    return pd.DataFrame(data)


def generate_opportunities_data(num_opportunities=100, salespeople=None):
    if salespeople is None:
        salespeople = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
    stages = ['Prospecting', 'First Contact', 'Qualified Leads', 'Demo', 'Closed Won', 'Closed Lost']
    sources = ['Webinar', 'Referral', 'Cold Call', 'Social Media', 'Advertisement']
    data = []
    for i in range(num_opportunities):
        data.append({
            'Opportunity ID': f'OPP-{i+1:03}',
            'Salesperson': np.random.choice(salespeople),
            'Stage': np.random.choice(stages),
            'Value': np.random.randint(10000, 100000),
            'Source': np.random.choice(sources),
            'Weighted Value': 0,  # Placeholder, will be calculated later
        })
    df = pd.DataFrame(data)
    # Calculate weighted value
    stage_weights = {'Prospecting': 0.1, 'First Contact': 0.25, 'Qualified Leads': 0.5, 'Demo': 0.75, 'Closed Won': 1.0, 'Closed Lost': 0.0}
    df['Weighted Value'] = df.apply(lambda row: row['Value'] * stage_weights[row['Stage']], axis=1)
    return df

def generate_recruitment_data(num_jobs=5, num_applicants=100):
    jobs = [f'Job {i+1}' for i in range(num_jobs)]
    stages = ['Applied', 'Screening', 'Interview', 'Offer', 'Hired']
    sources = ['LinkedIn', 'Indeed', 'Company Website', 'Referral']
    data = []
    for i in range(num_applicants):
        job = np.random.choice(jobs)
        stage = np.random.choice(stages)
        source = np.random.choice(sources)
        days_to_hire = np.random.randint(10, 60)
        data.append({
            'Applicant ID': f'APP-{i+1:03}',
            'Job': job,
            'Stage': stage,
            'Source': source,
            'Days to Hire': days_to_hire,
        })
    return pd.DataFrame(data)

def generate_aircall_data(num_calls=200, salespeople=None):
    if salespeople is None:
        salespeople = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
    data = []
    for i in range(num_calls):
        data.append({
            'Call ID': f'CALL-{i+1:03}',
            'Salesperson': np.random.choice(salespeople),
            'Call Time (seconds)': np.random.randint(30, 300),
            'Wait Time (seconds)': np.random.randint(0, 60),
            'Missed Call': np.random.choice([True, False], p=[0.1, 0.9]),
        })
    return pd.DataFrame(data)

def generate_product_performance_data():
    np.random.seed(42)
    dates = pd.date_range(start='2024-01-01', periods=12, freq='MS')  # Monthly data
    products = ['Product_1', 'Product_2', 'Product_3', 'Product_4', 'Product_5']
    data = []
    for date in dates:
        for product in products:
            revenue = np.random.randint(50000, 300000)  # Random revenue per month
            data.append({'Date': date, 'Product': product, 'Revenue': revenue})
    return pd.DataFrame(data)


df_pipeline = generate_mock_data1()
df_competition = generate_competition_data()
df_activity = generate_activity_data()
df_opportunities = generate_opportunities_data()
df_recruitment = generate_recruitment_data()
df_aircall = generate_aircall_data()
df_product_performance = generate_product_performance_data()


# --- Sidebar Filters ---
st.sidebar.header("Filters")
tab_select = st.sidebar.radio(
    "Select Dashboard:", ("Sales Pipeline", "Sales Competition", "Sales Activity", "Sales Opportunities", "Sales Recruitment", "Aircall", "Product Performance")
)

if tab_select == "Sales Pipeline":
    # ... (Sales Pipeline Dashboard code remains the same)
    start_date = st.sidebar.date_input("Start Date", df_pipeline["Date"].min())
    end_date = st.sidebar.date_input("End Date", df_pipeline["Date"].max())
    selected_sales_rep = st.sidebar.multiselect(
        "Select Sales Rep",
        df_pipeline["Salesperson"].unique(),
        default=df_pipeline["Salesperson"].unique(),
    )
    selected_region = st.sidebar.multiselect(
        "Select Region",
        df_pipeline["Region"].unique(),
        default=df_pipeline["Region"].unique(),
    )

    # Apply Filters
    df_filtered = df_pipeline[
        (df_pipeline["Salesperson"].isin(selected_sales_rep))
        & (df_pipeline["Region"].isin(selected_region))
        & (df_pipeline["Date"] >= pd.Timestamp(start_date))
        & (df_pipeline["Date"] <= pd.Timestamp(end_date))
    ].copy()

    # Weekly Sales Activity
    st.subheader("📈 First Contacts")
    df_monthly_contacts = (
        df_filtered.resample("ME", on="Date").sum().reset_index()
    )
    fig_contacts = px.line(
        df_monthly_contacts,
        x="Date",
        y="First Contact Made",
        title="First Contacts Made",
        markers=True,
    )
    st.plotly_chart(fig_contacts, use_container_width=True)

    # Demo by Rep
    st.subheader("🎥 Demos by Sales Rep")
    selected_demo_rep = st.selectbox(
        "Select Sales Rep for Demos", df_pipeline["Salesperson"].unique()
    )
    demo_data = (
        df_filtered[df_filtered["Salesperson"] == selected_demo_rep]
        .groupby(["Salesperson", "Company"])
        .agg({"Revenue": "sum", "Deals Closed": "sum"})
        .reset_index()
    )
    st.dataframe(demo_data, use_container_width=True)

    # Highest Value Opportunity
    st.subheader("💰 Highest Value Opportunity")
    highest_opportunity = df_filtered.loc[
        df_filtered["Opportunity Value"].idxmax()
    ]
    st.metric("Company", highest_opportunity["Company"])
    st.metric("Value", f"₹{highest_opportunity['Opportunity Value']:,.2f}")

    # Performance This Quarter
    st.subheader("📊 Performance This Quarter")
    pipeline_data = (
        df_filtered.groupby("Pipeline Stage")["Revenue"].sum().reset_index()
    )
    fig_pipeline = px.bar(
        pipeline_data,
        x="Pipeline Stage",
        y="Revenue",
        title="Pipeline Breakdown by Stage",
        color="Pipeline Stage",
    )
    st.plotly_chart(fig_pipeline, use_container_width=True)

    # Close Ratio & Average Sales Cycle
    st.subheader("🔍 Key Performance Indicators")
    total_deals = df_filtered["Deals Closed"].sum()
    closed_won_deals = df_filtered[
        df_filtered["Pipeline Stage"] == "Closed Won"
    ]["Deals Closed"].sum()
    close_ratio = (
        (closed_won_deals / total_deals) * 100 if total_deals > 0 else 0
    )
    average_cycle_length = np.random.randint(30, 90)

    col6, col7 = st.columns([2, 1])
    fig_donut = px.pie(
        values=[close_ratio, 100 - close_ratio],
        names=["Closed Won", "Others"],
        title="Close Ratio",
        hole=0.5,
    )
    col6.plotly_chart(fig_donut, use_container_width=True)
    col7.metric("⏳ Avg Sales Cycle (days)", f"{average_cycle_length}", delta=None)

    st.subheader("🔮 Scenario Analysis: Revenue Comparison")
    adjusted_growth = st.slider("Expected Revenue Growth (%)", -50, 100, 10)
    df_filtered.loc[:, "Projected Revenue"] = df_filtered["Revenue"] * (
        1 + adjusted_growth / 100
    )

    melted_projection = df_filtered[
        ["Salesperson", "Revenue", "Projected Revenue"]
    ].melt(id_vars="Salesperson", var_name="Revenue Type", value_name="Revenue Value")

    fig_comparison = px.bar(
        melted_projection,
        x="Salesperson",
        y="Revenue Value",
        color="Revenue Type",
        barmode="group",
        title="Original vs. Projected Revenue by Salesperson",
        labels={
            "Revenue Value": "Revenue",
            "Salesperson": "Salesperson",
            "Revenue Type": "Revenue Type",
        },
    )
    st.plotly_chart(
        fig_comparison, use_container_width=True, key="projection_comparison_chart"
    )

    # Order vs. Invoice Tracking
    st.subheader("📑 Orders vs. Invoices")
    order_invoice_data = df_filtered.groupby("Date").agg(
        {"Orders Placed": "sum", "Invoices Issued": "sum"}
    ).reset_index()

    fig_area = px.area(
        order_invoice_data,
        x="Date",
        y=["Orders Placed", "Invoices Issued"],
        labels={"value": "Count", "Date": "Date"},
    )

    st.plotly_chart(fig_area, use_container_width=True, key="orders_area_chart")
    st.success("🚀 Dashboard updated with enhanced pipeline insights!")

elif tab_select == "Sales Competition":
    st.title("🏆 Sales Competition Dashboard")
    competition_type = st.sidebar.selectbox(
        "Competition Type",
        ["Sales Leaderboard", "Individual Performance", "Raffle/Golf", "Team A vs Team B"],
    )
    selected_date_range = st.sidebar.date_input(
        "Date Range", [df_competition["Date"].min(), df_competition["Date"].max()]
    )
    start_date, end_date = selected_date_range

    df_filtered = df_competition[
        (df_competition["Date"] >= pd.Timestamp(start_date))
        & (df_competition["Date"] <= pd.Timestamp(end_date))
    ]

    if competition_type == "Sales Leaderboard":
        st.subheader("📊 Sales Leaderboard")
        leaderboard = (
            df_filtered.groupby("Salesperson")
            .agg({"Revenue": "sum", "Sales": "sum"})
            .sort_values(by="Revenue", ascending=False)
            .reset_index()
        )
        st.dataframe(leaderboard, use_container_width=True)

        fig_leaderboard = px.bar(
            leaderboard, x="Salesperson", y="Revenue", title="Revenue Leaderboard"
        )
        st.plotly_chart(fig_leaderboard, use_container_width=True)

    elif competition_type == "Individual Performance":
        st.subheader("📈 Individual Performance")
        selected_salesperson = st.selectbox(
            "Select Salesperson", df_filtered["Salesperson"].unique()
        )
        individual_data = df_filtered[
            df_filtered["Salesperson"] == selected_salesperson
        ].set_index("Date")

        st.write(f"### {selected_salesperson}'s Performance")
        col1, col2 = st.columns(2)
        col1.metric("Total Revenue", f"₹{individual_data['Revenue'].sum():,.2f}")
        col2.metric("Total Sales", individual_data["Sales"].sum())

        fig_revenue = px.line(
            individual_data,
            y="Revenue",
            title=f"{selected_salesperson} Revenue Over Time",
        )
        st.plotly_chart(fig_revenue, use_container_width=True)

        fig_sales = px.line(
            individual_data,
            y="Sales",
            title=f"{selected_salesperson} Sales Over Time",
        )
        st.plotly_chart(fig_sales, use_container_width=True)

    elif competition_type == "Raffle/Golf":
        st.subheader("🎟️ Raffle/Golf Competition")
        golf_balls = (
            df_filtered[df_filtered["Revenue"] > 5000]
            .groupby("Salesperson")["Revenue"]
            .count()
            .reset_index()
        )
        golf_balls.rename(columns={"Revenue": "Golf Balls"}, inplace=True)
        st.dataframe(golf_balls, use_container_width=True)

        st.write("### Putt-Putt Golf Leaderboard")
        winner = golf_balls.sample(n=1)
        st.write(f"The winner is {winner['Salesperson'].values[0]}!")

    elif competition_type == "Team A vs Team B":
        st.subheader("⚔️ Team A vs Team B")
        salespeople = df_filtered["Salesperson"].unique()
        team_a = np.random.choice(
            salespeople, size=len(salespeople) // 2, replace=False
        )
        team_b = [person for person in salespeople if person not in team_a]

        team_a_data = (
            df_filtered[df_filtered["Salesperson"].isin(team_a)]
            .groupby("Date")
            .agg({"Revenue": "sum"})
            .reset_index()
        )
        team_b_data = (
            df_filtered[df_filtered["Salesperson"].isin(team_b)]
            .groupby("Date")
            .agg({"Revenue": "sum"})
            .reset_index()
        )

        team_a_data["Team"] = "Team A"
        team_b_data["Team"] = "Team B"
        team_data = pd.concat([team_a_data, team_b_data])

        fig_team = px.line(
            team_data,
            x="Date",
            y="Revenue",
            color="Team",
            title="Team A vs Team B Revenue",
        )
        st.plotly_chart(fig_team, use_container_width=True)

        team_a_total = team_a_data["Revenue"].sum()
        team_b_total = team_b_data["Revenue"].sum()

        st.write(f"Team A Total Revenue: ₹{team_a_total:,.2f}")
        st.write(f"Team B Total Revenue: ₹{team_b_total:,.2f}")

        if team_a_total > team_b_total:
            st.write("Team A Wins!")
        elif team_b_total > team_a_total:
            st.write("Team B Wins!")
        else:
            st.write("It's a Tie!")
    # --- Sales Activity Dashboard ---
elif tab_select == "Sales Activity":
    st.title("🎯 Sales Activity Dashboard")

    # Filters
    start_date_activity = st.sidebar.date_input(
        "Start Date", df_activity["Date"].min()
    )
    end_date_activity = st.sidebar.date_input(
        "End Date", df_activity["Date"].max()
    )
    selected_salespeople_activity = st.sidebar.multiselect(
        "Select Salesperson",
        df_activity["Salesperson"].unique(),
        default=df_activity["Salesperson"].unique(),
    )

    # Apply Filters
    df_activity_filtered = df_activity[
        (df_activity["Date"] >= pd.Timestamp(start_date_activity))
        & (df_activity["Date"] <= pd.Timestamp(end_date_activity))
        & (df_activity["Salesperson"].isin(selected_salespeople_activity))
    ].copy()

    # Aggregated Activity Metrics
    st.subheader("📊 Aggregated Activity")
    total_calls = df_activity_filtered["Calls"].sum()
    total_emails = df_activity_filtered["Emails"].sum()
    total_demos = df_activity_filtered["Demos"].sum()
    total_social = df_activity_filtered["Social Interactions"].sum()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Calls", total_calls)
    col2.metric("Total Emails", total_emails)
    col3.metric("Total Demos", total_demos)
    col4.metric("Total Social", total_social)

    # Activity Over Time
    st.subheader("📈 Activity Over Time")
    activity_over_time = df_activity_filtered.groupby("Date").agg(
        {"Calls": "sum", "Emails": "sum", "Demos": "sum", "Social Interactions": "sum"}
    ).reset_index()
    activity_over_time_melted = activity_over_time.melt(
        id_vars="Date",
        var_name="Activity Type",
        value_name="Activity Count",
    )
    fig_activity_over_time = px.line(
        activity_over_time_melted,
        x="Date",
        y="Activity Count",
        color="Activity Type",
        title="Sales Activity Over Time",
    )
    st.plotly_chart(fig_activity_over_time, use_container_width=True)

    # Activity by Salesperson
    st.subheader("🧑‍💼 Activity by Salesperson")
    activity_by_salesperson = df_activity_filtered.groupby("Salesperson").agg(
        {"Calls": "sum", "Emails": "sum", "Demos": "sum", "Social Interactions": "sum"}
    ).reset_index()
    activity_by_salesperson_melted = activity_by_salesperson.melt(
        id_vars="Salesperson", var_name="Activity Type", value_name="Activity Count"
    )
    fig_activity_by_salesperson = px.bar(
        activity_by_salesperson_melted,
        x="Salesperson",
        y="Activity Count",
        color="Activity Type",
        title="Sales Activity by Salesperson",
    )
    st.plotly_chart(fig_activity_by_salesperson, use_container_width=True)

elif tab_select == "Sales Opportunities":
    st.title("💰 Sales Opportunities Dashboard")

    # Filters
    selected_salespeople_opp = st.sidebar.multiselect("Select Salesperson", df_opportunities["Salesperson"].unique(), default=df_opportunities["Salesperson"].unique())
    selected_stages_opp = st.sidebar.multiselect("Select Stage", df_opportunities["Stage"].unique(), default=df_opportunities["Stage"].unique())
    selected_sources_opp = st.sidebar.multiselect("Select Source", df_opportunities["Source"].unique(), default=df_opportunities["Source"].unique())

    df_opportunities_filtered = df_opportunities[
        (df_opportunities["Salesperson"].isin(selected_salespeople_opp)) &
        (df_opportunities["Stage"].isin(selected_stages_opp)) &
        (df_opportunities["Source"].isin(selected_sources_opp))
    ].copy()

    # Total Opportunities
    st.subheader("Total Opportunities")
    st.metric("Number of Opportunities", len(df_opportunities_filtered))

    # Total Value and Weighted Value
    st.subheader("Total Value and Weighted Value")
    total_value = df_opportunities_filtered["Value"].sum()
    total_weighted_value = df_opportunities_filtered["Weighted Value"].sum()
    col1, col2 = st.columns(2)
    col1.metric("Total Value", f"₹{total_value:,.2f}")
    col2.metric("Total Weighted Value", f"₹{total_weighted_value:,.2f}")

    # Opportunities by Stage (Colorful and Intuitive)
    st.subheader("Opportunities by Stage")
    stage_counts = df_opportunities_filtered["Stage"].value_counts().reset_index()
    stage_counts.columns = ["Stage", "Count"]

    fig_stage = px.bar(
        stage_counts,
        x="Stage",
        y="Count",
        title="Opportunities by Stage",
        color="Stage",  # Color by stage
        color_discrete_sequence=px.colors.qualitative.Pastel1, #added color
        labels={"Count": "Number of Opportunities", "Stage": "Sales Stage"}, #added better labels
    )
    st.plotly_chart(fig_stage, use_container_width=True)

    # Opportunities by Source (Colorful and Intuitive)
    st.subheader("Opportunities by Source")
    source_counts = df_opportunities_filtered["Source"].value_counts().reset_index()
    source_counts.columns = ["Source", "Count"]

    fig_source = px.bar(
        source_counts,
        x="Source",
        y="Count",
        title="Opportunities by Source",
        color="Source",  # Color by source
        color_discrete_sequence=px.colors.qualitative.Set2, #added color
        labels={"Count": "Number of Opportunities", "Source": "Opportunity Source"}, #added better labels
    )
    st.plotly_chart(fig_source, use_container_width=True)

    # Opportunities by Salesperson (Colorful and Intuitive)
    st.subheader("Opportunities by Salesperson")
    salesperson_counts = df_opportunities_filtered["Salesperson"].value_counts().reset_index()
    salesperson_counts.columns = ["Salesperson", "Count"]

    fig_salesperson = px.bar(
        salesperson_counts,
        x="Salesperson",
        y="Count",
        title="Opportunities by Salesperson",
        color="Salesperson",  # Color by salesperson
        color_discrete_sequence=px.colors.qualitative.Pastel1, #added color
        labels={"Count": "Number of Opportunities", "Salesperson": "Sales Representative"}, #added better labels
    )
    st.plotly_chart(fig_salesperson, use_container_width=True)

elif tab_select == "Sales Recruitment":
    st.title("🤝 Sales Recruitment Dashboard")

    # Filters
    selected_jobs_rec = st.sidebar.multiselect("Select Job", df_recruitment["Job"].unique(), default=df_recruitment["Job"].unique())
    selected_stages_rec = st.sidebar.multiselect("Select Stage", df_recruitment["Stage"].unique(), default=df_recruitment["Stage"].unique())
    selected_sources_rec = st.sidebar.multiselect("Select Source", df_recruitment["Source"].unique(), default=df_recruitment["Source"].unique())

    df_recruitment_filtered = df_recruitment[
        (df_recruitment["Job"].isin(selected_jobs_rec)) &
        (df_recruitment["Stage"].isin(selected_stages_rec)) &
        (df_recruitment["Source"].isin(selected_sources_rec))
    ].copy()

    # Average Days to Hire
    st.subheader("Average Days to Hire")
    avg_days_to_hire = df_recruitment_filtered["Days to Hire"].mean()
    st.metric("Average Days", f"{avg_days_to_hire:.2f} days")

    # Applicants by Job (Colorful and Intuitive)
    st.subheader("Applicants by Job")
    job_counts = df_recruitment_filtered["Job"].value_counts().reset_index()
    job_counts.columns = ["Job", "Count"]

    fig_job = px.bar(
        job_counts,
        x="Job",
        y="Count",
        title="Applicants by Job",
        color="Job", #added color
        color_discrete_sequence=px.colors.qualitative.T10, #added color
        labels={"Count": "Number of Applicants", "Job": "Job Title"} #added better labels
    )
    st.plotly_chart(fig_job, use_container_width=True)

    # Applicants by Stage (Colorful and Intuitive)
    st.subheader("Applicants by Stage")
    stage_counts = df_recruitment_filtered["Stage"].value_counts().reset_index()
    stage_counts.columns = ["Stage", "Count"]

    fig_stage = px.bar(
        stage_counts,
        x="Stage",
        y="Count",
        title="Applicants by Stage",
        color="Stage", #added color
        color_discrete_sequence=px.colors.qualitative.T10, #added color
        labels={"Count": "Number of Applicants", "Stage": "Recruitment Stage"} #added better labels
    )
    st.plotly_chart(fig_stage, use_container_width=True)

    # Applicants by Source (Colorful and Intuitive)
    st.subheader("Applicants by Source")
    source_counts = df_recruitment_filtered["Source"].value_counts().reset_index()
    source_counts.columns = ["Source", "Count"]

    fig_source = px.bar(
        source_counts,
        x="Source",
        y="Count",
        title="Applicants by Source",
        color="Source", #added color
        color_discrete_sequence=px.colors.qualitative.T10, #added color
        labels={"Count": "Number of Applicants", "Source": "Application Source"} #added better labels
    )
    st.plotly_chart(fig_source, use_container_width=True)

elif tab_select == "Aircall":
    st.title("📞 Aircall Dashboard")

    # Filters
    selected_salespeople_ac = st.sidebar.multiselect("Select Salesperson", df_aircall["Salesperson"].unique(), default=df_aircall["Salesperson"].unique())

    df_aircall_filtered = df_aircall[df_aircall["Salesperson"].isin(selected_salespeople_ac)].copy()

    # Metrics
    st.subheader("Call Metrics")
    avg_talk_time = df_aircall_filtered["Call Time (seconds)"].mean()
    avg_wait_time = df_aircall_filtered["Wait Time (seconds)"].mean()
    missed_call_rate = df_aircall_filtered["Missed Call"].mean() * 100

    col1, col2, col3 = st.columns(3)
    col1.metric("Average Talk Time", f"{avg_talk_time:.2f} seconds")
    col2.metric("Average Wait Time", f"{avg_wait_time:.2f} seconds")
    col3.metric("Missed Call Rate", f"{missed_call_rate:.2f}%")

    # Leaderboards
    st.subheader("Leaderboards")
    col4, col5 = st.columns(2)

    # Call Time Leaderboard
    call_time_leaderboard = df_aircall_filtered.groupby("Salesperson")["Call Time (seconds)"].sum().sort_values(ascending=False).reset_index()
    col4.subheader("Call Time")
    col4.dataframe(call_time_leaderboard, use_container_width=True)

    # Total Calls Leaderboard
    total_calls_leaderboard = df_aircall_filtered["Salesperson"].value_counts().reset_index()
    total_calls_leaderboard.columns = ["Salesperson", "Total Calls"]
    col5.subheader("Total Calls")
    col5.dataframe(total_calls_leaderboard, use_container_width=True)

    # Call Distribution
    st.subheader("Call Distribution")
    fig_call_time = px.histogram(df_aircall_filtered, x="Call Time (seconds)", title="Call Time Distribution")
    st.plotly_chart(fig_call_time, use_container_width=True)

elif tab_select == "Product Performance":
    st.title("📈 Product Performance Dashboard")

    # Filters
    selected_products = st.sidebar.multiselect("Select Product", df_product_performance["Product"].unique(), default=df_product_performance["Product"].unique())

    df_product_filtered = df_product_performance[df_product_performance["Product"].isin(selected_products)].copy()

    # Total Revenue
    total_revenue = df_product_filtered["Revenue"].sum()
    st.metric("Total Revenue", f"₹{total_revenue:,.2f}")

    # Revenue by Product
    st.subheader("Revenue by Product")
    product_revenue = df_product_filtered.groupby("Product")["Revenue"].sum().reset_index()
    fig_product_revenue = px.bar(product_revenue, x="Product", y="Revenue", title="Revenue by Product")
    st.plotly_chart(fig_product_revenue, use_container_width=True)

    # Revenue Over Time
    st.subheader("Revenue Over Time")
    fig_revenue_time = px.line(df_product_filtered, x="Date", y="Revenue", color="Product", title="Revenue Over Time")
    st.plotly_chart(fig_revenue_time, use_container_width=True)