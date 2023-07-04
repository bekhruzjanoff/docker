from main import app


#Registrasii polzovately
@app.post('/register-user')
async def register_user_api(phone_number: int, name: str, pincode: int, password: str):
    pass


#Vxod v akk
@app.post('/login')
async def login_user_api(phone_number: int, password: str):
    pass


#Vivod informatsii polzovatelya
@app.get('/user-cabinet')
async def get_user_cabinet_api(user_id: int):
    pass


#poluchit karti po nomeru
@app.get('/get-user-cards-by-phone')
async def get_user_cards_by_phone_number_api(phone_number: int):
    pass





