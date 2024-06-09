import streamlit as st
import numpy as np
import pandas as pd
import pickle

pickle_in=open('house_price_pred.pkl','rb')
model=pickle.load(pickle_in)



def main():
    html_tnp = """
    <h1 style="text-align:center;">House Price</h1>
    <div style="background-color:tomato; padding:10px; margin-bottom:10px;">
        <h2 style="color:white; text-align:center; ">House Price Prediction</h2>
    </div>
    <style>
         .stButton>button {
               background-color: #4CAF50; /* Green */
               border: none;
               color: white;
               text-align: center;
               text-decoration: none;
               font-size: 14px;
               transition-duration: 0.4s;
               cursor: pointer;
               margin: 0 auto;
               display:block;
        }
        .stButton>button:hover {
               background-color: white;
               color: black;
               border: 2px solid #4CAF50;
        }
     </style>
        

    """

    html_footer="""
    <div style=" text-align: center;
                 padding: 10px;
                 margin-top:10px;
                 font-size: 15px;
                 color:white;
                 background-color:grey;">
                 &copy; 2024 House Price Prediction by Satish Gokavarapu
    </div>"""
    st.markdown(html_tnp, unsafe_allow_html=True)

    house_type={
             "Appartment":0,
             "House or Villa " : 1,
             "Builder Floors":2
             }
    

    htype=st.selectbox("Select House Type",house_type.keys())
    htype_val=house_type[htype]
    bedrooms=st.number_input("No of Bedrooms",min_value=0,step=1)
    bathrooms=st.number_input("No of Bathrooms",min_value=0,step=1)

    furniture={
              "Unfurnished":0,
              "Semi-furnished":1,
              "Furnished":2
              }
    fur=st.selectbox("Furniture",furniture.keys())
    furnitures=furniture[fur]
    sba=st.number_input("Total Area in sqrft",min_value=0,step=1)
    ca=st.number_input("Useful Area in sqrft",min_value=0,step=1)
    car=st.number_input("No of Car Parking available",min_value=0,step=1)
    maintanence=st.number_input("Maintainence per month",min_value=0,step=1)
    tfloors=st.number_input("Total Floors",min_value=1,step=1)
    floor=st.number_input("Floor",min_value=1,step=1)


    if st.button('Predict'):

        input_data=np.array([[htype_val,bedrooms,bathrooms,furnitures,sba,ca,car,maintanence,tfloors,floor]])
        input_data_converted = input_data.astype(np.float32)
        pred = model.predict(input_data_converted,check_input=False)
        price=np.round(pred)

        st.success("The price for the following House can be {}/-".format(price[0]))
    st.markdown(html_footer,unsafe_allow_html=True)

     
if __name__ == '__main__' :
    main()

