from flask_restx import Namespace,Resource


order_namespace = Namespace('order',description='a namespace for orders')

@order_namespace.route("/order")
class orderGetCreate(Resource):
    def get(self):
        """Get all Orders"""
        return { "msg":"hello Orders"}
    
    def post(self):
        """ Create New Order"""
        pass

@order_namespace.route('/order/<int:order_id>')
class GetUpdateDelete(Resource):
    def get(self, order_id):
        """Retrieve Order by id"""
        pass

    def put(self,order_id):
        """Update  order by id"""
        pass

    def delete(self,order_id):
        """Delete order by id"""
        pass


@order_namespace.route("/user/<int:user_id>/order/<int:order_id>")
class GetSpecificOrderByUser(Resource):
    def get(self,user_id, order_id):
        """user order by userid and orderid"""
        pass
@order_namespace.route("/user/<int:user_id>/orders")
class GetSpecificUserOrders(Resource):
    def get(self,user_id):
        """Get all orders of specific user"""
        pass
