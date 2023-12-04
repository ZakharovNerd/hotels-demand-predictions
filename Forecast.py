# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
from heatmapcalendar import create_calendar_heatmap


LOGGER = get_logger(__name__)


def run():
    st.title("Calendar Heatmap")

    # Sample data (you can modify this part to accept user input or different data sources)
    values = [30.2, 37.6, 32.7, 32.2, 37.1, 30.9, 32.9, 35.5, 30.9, 35.7, 31.1, 33.9, 32.7, 30.1, 40.9, 36.2, 36.5, 32.9, 37.4, 33.0, 36.4, 31.9, 30.2, 33.9, 33.7, 31.3, 33.7, 31.0, 34.0, 32.5]

    days_of_month = list(range(1, 31))

    # Creating the heatmap
    fig, ax = create_calendar_heatmap(values, days_of_month)

    # Displaying the heatmap in Streamlit
    st.pyplot(fig)

if __name__ == "__main__":
    run()
