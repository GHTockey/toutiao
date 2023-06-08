from app.resources.user import user_module


@user_module.route('/ttt')
def index():
    return "user_module"
