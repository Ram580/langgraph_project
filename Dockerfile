# Use official Python image as base
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Expose the port Streamlit will run on
EXPOSE 7860

# Streamlit-specific environment variables for Hugging Face Spaces
ENV PORT 7860
ENV STREAMLIT_SERVER_PORT 7860
ENV STREAMLIT_SERVER_ADDRESS 0.0.0.0

# Run the Streamlit app
CMD ["streamlit", "run", "src/langgraphagenticai/app.py"]
