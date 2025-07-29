#!/bin/bash

# Set default port if PORT is not set
PORT=${PORT:-8501}

# Start Streamlit
exec streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
