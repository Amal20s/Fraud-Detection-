import streamlit as st
import pandas as pd
import joblib 


model = joblib.load("fraud_detection_pipeline.pkl")

model.predict
st.title("Fraud Detection Predection App")

st.markdown("Please Enter the transaction Details and use the predict button")

st.divider()

transaction_type=st.selectbox("Transaction Type",["PAYMENT","TRANSFER","CASH_OUT"])


Amount=st.number_input("Amount",min_value=0.0,value=1000.0)
oldbalanceOrg=st.number_input("Old balance(sender)",min_value=0.0,value=1000.0)
newbalanceOrig=st.number_input("New Balance() sender)",min_value=0.0,value=1000.0)
oldbalanceDest=st.number_input("old balance (receiver)",min_value=0.0,value=1000.0)
newbalanceDest=st.number_input("new balance (receiver)",min_value=0.0,value=1000.0)


if st.button("predict"):
    input_data=pd.DataFrame([{
        "type":transaction_type,
        "amount": Amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest":newbalanceDest
    }])

    prediction=model.predict(input_data)[0]

    st.subheader(f"prediction:'{int(prediction)})'")

    if prediction==1:
        st.error("this transactio can be fraudlant")
    else:
        st.success("this transaction appears to be not fraud")
        