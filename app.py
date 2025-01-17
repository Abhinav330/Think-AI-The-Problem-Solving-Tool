import os
from dotenv import load_dotenv
import time
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
groq_api_key= os.getenv("GROQ_API_KEY")

p1 = os.getenv("pmpt1")
p2 = os.getenv("pmpt2")
p3 = os.getenv("pmpt3")
p4 = os.getenv("pmpt4")
p5 = os.getenv("pmpt5")
p6 = os.getenv("pmpt6")
p7 = os.getenv("pmpt7")
p8 = os.getenv("pmpt8")
p9 = os.getenv("pmpt9")
p10 = os.getenv("pmpt10")
p11 = os.getenv("pmpt11")
p12 = os.getenv("pmpt12")
p13 = os.getenv("pmpt13")
p14 = os.getenv("pmpt14")
p15 = os.getenv("pmpt15")
p16 = os.getenv("pmpt16")
p17 = os.getenv("pmpt17")
p18 = os.getenv("pmpt18")
p19 = os.getenv("pmpt19")
p20 = os.getenv("pmpt20")
p21 = os.getenv("pmpt21")
p22 = os.getenv("pmpt22")
p23 = os.getenv("pmpt23")
p24 = os.getenv("pmpt24")
p25 = os.getenv("pmpt25")

prompt1 = ChatPromptTemplate.from_messages([("system",p1),("user", "Question:{query1}")])
prompt2 = ChatPromptTemplate.from_messages([("system",p2),("user", "Question:{query1}")])
prompt3 = ChatPromptTemplate.from_messages([("system",p3),("user", "Question:{query1}")])
prompt4 = ChatPromptTemplate.from_messages([("system",p4),("user", "Question:{query1}")])
prompt5 = ChatPromptTemplate.from_messages([("system",p5),("user", "Question:{query1}")])
prompt6 = ChatPromptTemplate.from_messages([("system",p6), ("user", "Question:{query1}")])
prompt7 = ChatPromptTemplate.from_messages([("system",p7), ("user", "Question:{query1}")])
prompt8 = ChatPromptTemplate.from_messages([("system",p8), ("user", "Question:{query1}")])
prompt9 = ChatPromptTemplate.from_messages([("system",p9), ("user", "Question:{query1}")])
prompt10 = ChatPromptTemplate.from_messages([("system", p10), ("user", "Question:{query1}")])
prompt11 = ChatPromptTemplate.from_messages([("system", p11), ("user", "Question:{query1}")])
prompt12 = ChatPromptTemplate.from_messages([("system", p12), ("user", "Question:{query1}")])
prompt13 = ChatPromptTemplate.from_messages([("system", p13), ("user", "Question:{query1}")])
prompt14 = ChatPromptTemplate.from_messages([("system", p14), ("user", "Question:{query1}")])
prompt15 = ChatPromptTemplate.from_messages([("system", p15), ("user", "Question:{query1}")])
prompt16 = ChatPromptTemplate.from_messages([("system", p16), ("user", "Question:{query1}")])
prompt17 = ChatPromptTemplate.from_messages([("system", p17), ("user", "Question:{query1}")])
prompt18 = ChatPromptTemplate.from_messages([("system", p18), ("user", "Question:{query1}")])
prompt19 = ChatPromptTemplate.from_messages([("system", p19), ("user", "Question:{query1}")])
prompt20 = ChatPromptTemplate.from_messages([("system", p20), ("user", "Question:{query1}")])
prompt21 = ChatPromptTemplate.from_messages([("system", p21), ("user", "Question:{query1}")])
prompt22 = ChatPromptTemplate.from_messages([("system", p22), ("user", "Question:{query1}")])
prompt23 = ChatPromptTemplate.from_messages([("system", p23), ("user", "Question:{query1}")])
prompt24 = ChatPromptTemplate.from_messages([("system", p24), ("user", "Question:{query1}")])
prompt25 = ChatPromptTemplate.from_messages([("system", p25), ("user", "Question:{query1}")])



llm1 = ChatGroq(model_name="llama3-70b-8192", groq_api_key=groq_api_key)
output_parser =  StrOutputParser()

chain1 = prompt1| llm1| output_parser
chain2 = prompt2| llm1| output_parser
chain3 = prompt3| llm1| output_parser
chain4 = prompt4| llm1| output_parser
chain5 = prompt5| llm1| output_parser
chain6 = prompt6| llm1| output_parser
chain7 = prompt7| llm1| output_parser
chain8 = prompt8| llm1| output_parser
chain9 = prompt9| llm1| output_parser
chain10 = prompt10| llm1| output_parser
chain11 = prompt11| llm1| output_parser
chain12 = prompt12| llm1| output_parser
chain13 = prompt13| llm1| output_parser
chain14 = prompt14| llm1| output_parser
chain15 = prompt15| llm1| output_parser
chain16 = prompt16| llm1| output_parser
chain17 = prompt17| llm1| output_parser
chain18 = prompt18| llm1| output_parser
chain19 = prompt19| llm1| output_parser
chain20 = prompt20| llm1| output_parser
chain21 = prompt21| llm1| output_parser
chain22 = prompt22| llm1| output_parser
chain23 = prompt23| llm1| output_parser
chain24 = prompt24| llm1| output_parser
chain25 = prompt25| llm1| output_parser



def  generate_ai_content(thinking_type, usr_ip):
    if thinking_type == "Analytical Thinking": return chain1.invoke({"query1": usr_ip})
    elif headline == "Creative Thinking":return chain2.invoke({"query1": usr_ip})
    elif headline == "Critical Thinking": return chain3.invoke({"query1": usr_ip})
    elif headline == "Logical Thinking": return chain4.invoke({"query1": usr_ip})
    elif headline == "Lateral Thinking": return chain5.invoke({"query1": usr_ip})
    elif headline == "Divergent Thinking": return chain6.invoke({"query1": usr_ip})
    elif headline == "Convergent Thinking": return chain7.invoke({"query1": usr_ip})
    elif headline == "Empathetic Thinking": return chain8.invoke({"query1": usr_ip})
    elif headline == "Systems Thinking": return chain9.invoke({"query1": usr_ip})
    elif headline == "Intuitive Thinking": return chain10.invoke({"query1": usr_ip})
    elif headline == "Strategic Thinking": return chain11.invoke({"query1": usr_ip})
    elif headline == "Collaborative Thinking": return chain12.invoke({"query1": usr_ip})
    elif headline == "Reverse Thinking": return chain13.invoke({"query1": usr_ip})
    elif headline == "Practical Thinking": return chain14.invoke({"query1": usr_ip})
    elif headline == "Mind Mapping": return chain15.invoke({"query1": usr_ip})
    elif headline == "Trial-and-Error Thinking": return chain16.invoke({"query1": usr_ip})
    elif headline == "Root Cause Analysis": return chain17.invoke({"query1": usr_ip})
    elif headline == "Optimistic Thinking": return chain18.invoke({"query1": usr_ip})
    elif headline == "Pessimistic Thinking": return chain19.invoke({"query1": usr_ip})
    elif headline == "Abstract Thinking": return chain20.invoke({"query1": usr_ip})
    elif headline == "Habitual Thinking": return chain21.invoke({"query1": usr_ip})
    elif headline == "Scenario Thinking": return chain22.invoke({"query1": usr_ip})
    elif headline == "Mathematical Thinking": return chain23.invoke({"query1": usr_ip})
    elif headline == "Ethical Thinking": return chain24.invoke({"query1": usr_ip})
    elif headline == "Design Thinking": return chain25.invoke({"query1": usr_ip})
        

st.title("Think AI")
st.text("Think AI is designed to explore all the posible ways to approch a problem to find the perfect solution.")
st.write("### Ask anything")
col1, col2 = st.columns([4, 1])
with col1:
    user_input = st.text_area("Enter your text:", key="input_text", height=68)
with col2:
    submit = st.button("Submit")


if submit and user_input.strip():
    counter = 0
    st.write("---")
    st.write("### Generated Content")
    headlines = ["Analytical Thinking", "Creative Thinking", "Critical Thinking","Logical Thinking", 
                   "Lateral Thinking","Divergent Thinking", "Convergent Thinking", "Empathetic Thinking", 
                   "Systems Thinking", "Intuitive Thinking","Strategic Thinking", "Collaborative Thinking", 
                   "Reverse Thinking", "Practical Thinking", "Mind Mapping","Trial-and-Error Thinking", 
                   "Root Cause Analysis", "Optimistic Thinking", "Pessimistic Thinking", "Abstract Thinking",
                   "Habitual Thinking", "Scenario Thinking", "Mathematical Thinking", "Ethical Thinking", 
                   "Design Thinking", 
                   ]
    for headline in headlines:

        if counter >=5:
            time.sleep(3)
            counter =0 
        
        st.write(f"#### {headline}")

        ai_content = generate_ai_content(headline, user_input)
        st.markdown(ai_content,unsafe_allow_html=True)
        # st.text_area(f" ", value=ai,key=headline)
        counter+=1

        st.markdown(
            """
            <hr style="border: none; border-top: 3px double #000; margin-top: 20px; margin-bottom: 20px;">
            """,
            unsafe_allow_html=True
        )

# End the box container
st.markdown('</div>', unsafe_allow_html=True)