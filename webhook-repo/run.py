from app import create_app

# Create the Flask app using the factory function
app = create_app()

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(host='0.0.0.0', port=5000, debug=True)
