from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import random
from prime_test import prime
  
app = Flask(__name__)
api = Api(app)

class Auth(Resource):
  
    def post(self):
        data = request.get_json()
        return jsonify({'status': 'Success', "sessionToken": "a068aa1d-990f-4179-88a3-23b83552892f"})

class Access(Resource):

    def post(self): 
        data = request.get_json()
        return jsonify({ "success": True, "access_token": "eyJraWQiOiJtb2NrLW9hdXRoMi1zZXJ2ZXIta2V5IiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIwY2Y0MzQzMi1lZWRkLTQyOWUtYmY5MS1iM2E1NzQ2ZTgyNTgiLCJzY3AiOiJVc2VyLlJlYWQiLCJ2ZXIiOiIyLjAiLCJhaW8iOiJkZjcxMWIyNy0xOWZiLTQzYTQtOGY4OS0yOWUyNTA4YTYzMWIiLCJhenBhY3IiOiIxIiwiaXNzIjoiaHR0cHM6XC9cL2Zha2VkaW5ncy5kZXYtZ2NwLm5haXMuaW9cL2Zha2UiLCJvaWQiOiI4OGIxY2E1NS04YmQ0LTQ2NDEtYjFiZC1mMDA0YWNmNjQ1ZmQiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJub3Rmb3VuZCIsImF1ZCI6Im5vdGZvdW5kIiwibmJmIjoxNjA5ODM3NjI0LCJhenAiOiJjbGllbnQgaWQgcMOlIGRlbiBzb20gc3DDuHIiLCJuYW1lIjoibm90Zm91bmQiLCJleHAiOjE2MTM0Mzc2MjQsImlhdCI6MTYwOTgzNzYyNCwianRpIjoiMzYxNzNhMGQtZjUwMi00MmE5LTliY2QtOGZkY2I4MTVkN2NkIn0.dTVyG7aXiNaTiwiYZnZEcvx2kAHu8xyM6EjGx4-Xl6Lh-u3G9jXLwfJvOCMDyYJTpP8AMdnndjsI-yiQEroU2qds2QCHbRTR7ZDXCmjbslk-u-yLF-6f6y1xen749hSultAtCoY5UGfWT9et5368UqFgs2x3mbqZQQ3DnetAeBX9RIUkjugObaJo30kdWj4oduopIYiD0H7kyeCKGxZDbc0LElNQP8kt6RjeMe13HdHYNeXZWuQNSCImMr1R-AdQ2XR_uBDXGDCC7mnyW3ONLQL9BUS4D80qHXNtCWlWD09XsI9k8FOBT_kD3BeIoXA8jD4K-9W4fmaU2_K_8K6eqQ"})

class Scan(Resource):
  
    def post(self):
        data = request.get_json()
        return jsonify({'jobID': "1234", "success": True})
    
class ScanStatus(Resource):
  
    def post(self):
        data = request.get_json()
        status = 'Finished' if prime.test(random.randint(0, 100)) else 'Submitted'
        return jsonify({'status': status})
    
class ScanReport(Resource):
  
    def post(self):
        data = request.get_json()
        report = [{"jobID": '1234', "summary": {"count": 10}}]
        return jsonify(report)
          
# adding the defined resources along with their corresponding urls
api.add_resource(Auth, '/api/v1/authn')
api.add_resource(Access, '/token')
api.add_resource(Scan, '/api/v1/scans/repo')
api.add_resource(ScanStatus, '/api/v1/scans/status')
api.add_resource(ScanReport, '/api/v1/scans/report')

# driver function
if __name__ == '__main__':
  
    app.run(host='0.0.0.0', port = 80, debug = False)