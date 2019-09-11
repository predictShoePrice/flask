from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'This is a flask app'
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://username:password@hostname/database"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@118.25.112.15:3306/shoes'


# 配置flask配置对象中键：SQLALCHEMY_COMMIT_TEARDOWN,设置为True,应用会自动在每次请求结束后提交数据库中变动
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 获取SQLAlchemy实例对象，接下来就可以使用对象调用数据

db = SQLAlchemy(app)


# 创建模型对象
class ShoesDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(300), nullable=False)
    product_model = db.Column(db.String(255),  nullable=False)
    product_name = db.Column(db.String(255),  nullable=False)
    initial_price = db.Column(db.String(255),  nullable=False)
    product_price = db.Column(db.String(255),  nullable=False)
    paltams = db.Column(db.String(2048),  nullable=False)
    sizes_json = db.Column(db.String(2048),  nullable=False)
    source = db.Column(db.String(255),  nullable=False)
    add_time = db.Column(db.String(255),  nullable=False)


@app.route('/shoes_detail/list')
def get_shoes_detail_list():
    page = int(request.args.get('page', '1'))
    size = int(request.args.get('size', '10'))
    keyword = request.args.get('keyword', '')
    query_result = ShoesDetail.query\
        .filter(ShoesDetail.product_model.ilike(f'%{keyword}%'))\
        .order_by(ShoesDetail.id.desc())\
        .paginate(page, size)
    results = []
    for result in query_result.items:
        results.append({
            'id': result.id,
            'product_id': result.product_id,
            'product_model': result.product_model,
            'product_name': result.product_name,
            'initial_price': result.initial_price,
            'product_price': result.product_price,
            'paltams': result.paltams,
            'sizes_json': result.sizes_json,
            'source': result.source,
            'add_time': result.add_time
        })
    return json.dumps({'data': {'list': results, 'total': query_result.total}})


if __name__ == '__main__':
    app.run()
