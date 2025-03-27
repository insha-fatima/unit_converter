import streamlit as st
st.title("Unit Converter")
st.write("In unit converter we can covert one unit into another unit e.g  centimeter to meter, gram to kilogram and soo on......")

def convert_units(value, unit_from, unit_to):
    conversions = {
        "centi_meters": {"meters": 0.01, "centi_meters": 1},
        "meters": {"centi_meters": 100, "meters": 1},
        "seconds": {"hours": 0.000277778, "seconds": 1},
        "hours": {"seconds": 3600, "hours": 1},
        "grams": {"kilo_grams": 0.001, "grams": 1},
        "kilo_grams": {"grams": 1000, "kilo_grams": 1},

    }
    key = f"{unit_from}_{unit_to}"

    if unit_from in conversions and unit_to in conversions[unit_from]:
        return value * conversions[unit_from][unit_to]

    else:
        return "conversions is not supported"
    
value = st.number_input("Enter the value: ")

unit_from = st.selectbox("Convert from:" , ["centi_meters","meters","hours","seconds","grams","kilo_grams"])

unit_to = st.selectbox("Convert to:" , ["centi_meters","meters","hours","seconds","grams","kilo_grams"])

if st.button("Convert"):
    result = convert_units(value , unit_from, unit_to)
    st.write(f"Converted value , {result}")











    