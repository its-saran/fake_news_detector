import streamlit as st
import json
from joblib import load


def load_config(path):
    with open(path, 'r') as file:
        return json.load(file)


class App:
    def __init__(self, config):
        self.config = config
        self.pipeline = load(config['models']['model1'])

    def predict(self, txt):
        res = self.pipeline.predict([txt])
        print(res)
        return res[0]

    def show(self):
        txt = st.text_area('Enter the news here', height=300)

        st.write(f"You wrote {len(txt)} characters.")

        prediction_txt = ''

        if st.button("Check", type="primary"):
            prediction = self.predict(txt)
            color = ''

            if prediction == 0:
                prediction_txt = 'Legit'
                color='blue'

            elif prediction == 1:
                prediction_txt = 'Fake'
                color = 'red'

            st.header(f"The above news is :{color}[{prediction_txt}]")

            print(f"Predicted the news as {prediction_txt} ")


if __name__ == '__main__':
    config = load_config("config/config.json")
    web_app = App(config)
    web_app.show()
