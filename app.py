import streamlit as st
import pickle
import pandas as pd
import plotly.graph_objects as go



st.set_page_config(
    page_title="Laptop Price Predictor",
    page_icon="💻",
    layout="wide"
)



# Load model
model = pickle.load(open('model.pkl', 'rb'))
columns = pickle.load(open('columns.pkl', 'rb'))

st.markdown("""
# 💻 Laptop Price Predictor

### Predict laptop prices using Machine Learning

---
""")


# Company
left_col, right_col = st.columns([1.2, 1])
with left_col:
    company_list = ['Apple', 'HP', 'Dell', 'Lenovo', 'Asus', 'Acer']
    selected_company = st.selectbox("Company", company_list)
    Company = {name: i for i, name in enumerate(company_list)}[selected_company]

    # Type
    type_list = ['Ultrabook', 'Notebook', 'Gaming', '2 in 1 Convertible', 'Workstation', 'Netbook']
    selected_type = st.selectbox("Type", type_list)
    TypeName = {name: i for i, name in enumerate(type_list)}[selected_type]

    # Layout
    col1, col2 = st.columns(2)

    with col1:
        Inches = st.number_input("Screen Size (Inches)", min_value=10.0, value=15.6)
        Ram = st.number_input("RAM (GB)", min_value=1, value=8)
        Weight = st.number_input("Weight (kg)", min_value=0.5, value=2.0)
        SSD = st.number_input("SSD (GB)", min_value=0, value=256)
        HDD = st.number_input("HDD (GB)", min_value=0, value=0)

    with col2:
        ips_option = st.selectbox("IPS Display", ["No", "Yes"])
        IPS = 1 if ips_option == "Yes" else 0
        PPI = st.number_input("PPI", min_value=50.0, value=150.0)

    # CPU Brand
    selected_cpu_brand = st.selectbox(
    "CPU Brand",
    ['Intel', 'AMD', 'Other']
)

    Cpu_brand = {
    'Intel': 0,
    'AMD': 1,
    'Other': 2
    }[selected_cpu_brand]

    # CPU Type
    selected_cpu_type = st.selectbox(
    "CPU Type",
    ['i3', 'i5', 'i7', 'Ryzen', 'Other']
)

    Cpu_type = {
    'i3': 0,
    'i5': 1,
    'i7': 2,
    'Ryzen': 3,
    'Other': 4
    }[selected_cpu_type]

   # GPU Brand
    selected_gpu_brand = st.selectbox(
    "GPU Brand",
    ['Intel', 'AMD', 'Nvidia']
)

    Gpu_brand = {
    'Intel': 0,
    'AMD': 1,
    'Nvidia': 2
    }[selected_gpu_brand]
# OS
    OpSys = {'Other':0,'Mac':1,'Windows':2}[st.selectbox("Operating System", ['Windows','Mac','Other'])]



# PREDICTION BLOCK



with right_col:

    if st.button("Predict"):
    
        input_df = pd.DataFrame(
        [[
            Company,
            TypeName,
            Inches,
            Ram,
            OpSys,
            Weight,
            SSD,
            HDD,
            Cpu_brand,
            Cpu_type,
            Gpu_brand,
            IPS,
            PPI
        ]],
        columns=columns
        )

        prediction = model.predict(input_df)
        if prediction[0] < 40000:
            category = "💸 Budget Laptop"

        elif prediction[0] < 80000:
            category = "⚖️ Mid-Range Laptop"

        else:
            category = "💎 Premium Laptop"

    # Price Card
        st.markdown(f"""
        <div style="
        background:linear-gradient(135deg,#1d4ed8,#2563eb);
        padding:25px;
        border-radius:15px;
        text-align:center;
        color:white;
        margin-bottom:20px;">

        <h3>Estimated Price</h3>

        <h1>₹ {int(prediction[0]):,}</h1>

        <div style="
        display:inline-block;
        background:rgba(255,255,255,0.2);
        padding:8px 18px;
        border-radius:20px;
        font-size:16px;">
        {category}
    
        </div>

        </div>

        """, unsafe_allow_html=True)

    # Category
       # if prediction[0] < 40000:
       #     st.warning("💸 Budget Laptop")
            

        #elif prediction[0] < 80000:
         #   st.info("⚖️ Mid-Range Laptop")
            

        #else:
         #   st.success("💎 Premium Laptop")
            

        st.subheader("📊 Hardware Strength Overview")

        ram_score = min(int((Ram / 32) * 100), 100)

        st.write("🧠 RAM")
        st.progress(ram_score)

        cpu_score = {
             "i3": 40,
             "i5": 70,
             "i7": 100,
             "Ryzen": 85,
             "Other": 30
        }[selected_cpu_type]

        st.write("⚙️ CPU Type")
        st.progress(cpu_score)

        ssd_score = min(int((SSD / 1024) * 100), 100)

        st.write("💾 SSD")
        st.progress(ssd_score)

        gpu_score = {
            "Intel": 40,
            "AMD": 70,
            "Nvidia": 100
        }[selected_gpu_brand]

        st.write("🎮 GPU")
        st.progress(gpu_score)
        
       
        st.subheader("💻 Laptop Configuration")
       

       

        spec1, spec2 = st.columns(2)

        with spec1:

            st.markdown(f"""
            <div style="
            background:#1f2937;
            padding:18px;
            border-radius:12px;
            margin-bottom:12px;">
            🏢 <b>Company</b><br>
            {selected_company}
            </div>

            
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style="
            background:#1f2937;
            padding:18px;
            border-radius:12px;
            margin-bottom:12px;">
            💻 <b>Type</b><br>
            {selected_type}
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style="
            background:#1f2937;
            padding:18px;
            border-radius:12px;
            margin-bottom:12px;">
            🧠 <b>RAM</b><br>
            {Ram} GB
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style="
            background:#1f2937;
            padding:18px;
            border-radius:12px;
            margin-bottom:12px;">
            💾 <b>Storage</b><br>
            SSD: {SSD} GB<br>
            HDD: {HDD} GB
            </div>
            """, unsafe_allow_html=True)

        with spec2:
  
            st.markdown(f"""
            <div style="
            background:#1f2937;
            padding:18px;
            border-radius:12px;
            margin-bottom:12px;">
            ⚙️ <b>CPU</b><br>
            {selected_cpu_type}
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style="
            background:#1f2937;
            padding:18px;
            border-radius:12px;
            margin-bottom:12px;">
            🎮 <b>GPU</b><br>
            {selected_gpu_brand}
            </div>
            """, unsafe_allow_html=True)

    

       