#library
import streamlit as st

#write 
st.write("program streamlit untuk mengalikan bilangan bulat")

#input bilangan pertama
number1= st.number_input ("masukkan bilangan pertama")
st.write (f"bilangan pertama adalah {number1}")

#input bilangan kedua
number2= st.number_input ("masukkan bilangan kedua")
st.write (f"bilangan pertama adalah {number2}")

#hasil kali 
hasil=number1*number2

if st.button("hitung"):
    st.write(f"hasil kali antara {number1} dan {number2} adalah {hasil} selamat kamu benar :100:")
    st.snow()
else:
    st.write("silahkan pencet tombol hitung!")
    
    