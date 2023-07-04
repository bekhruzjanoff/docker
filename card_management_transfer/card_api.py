from main import app


@app.post('/add-user-card')
async def add_user_card_api(user_id: int,cardholder:str,card_name:str,card_number:int, exp_date:int,otp:int):
    pass


#generatsiya proverochnogo koda
@app.get('/one-time-password')
async def get_one_time_password(transfer_id:int):
    pass


@app.post('/transfer-user-money')
async def transfer_money_api(card_from: int,card_id:int,otp:int):
    pass


@app.delete('/delete-user-card')
async def delete_user_card(card_id:int,user_id:int):
    pass

#vivod
@app.get('/get-user-cards')
async def get_exact_or_all_cards(user_id:int,card:int = 0):
    pass

