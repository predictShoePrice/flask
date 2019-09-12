from application import app
from web.controllers.static import route_static
from web.controllers.user.User import route_user
from web.controllers.index import route_index
from web.controllers.account.Account import route_account
from web.controllers.goods.Goods import route_goods


app.register_blueprint(route_index, url_prefix="/")
app.register_blueprint(route_static, url_prefix="/static")
app.register_blueprint(route_user, url_prefix="/user")
app.register_blueprint(route_account, url_prefi="/account")
app.register_blueprint(route_goods, url_prefi="/goods")