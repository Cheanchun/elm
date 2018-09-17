from apps import create_app, create_api_app

cms_app = create_app()
api_app = create_api_app()

if __name__ == '__main__':
    api_app.run(host="0.0.0.0")
    cms_app.run(host="0.0.0.0")
