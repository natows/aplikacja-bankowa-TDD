from flask import Flask, request, jsonify
from app.AccountRegistry import AccountRegistry
from app.PersonalAccount import PersonalAccount
app = Flask(__name__)

@app.route("/api/accounts", methods=['POST'])
def create_account():
    data = request.get_json()
    print(f"Create account request: {data}")
    check = AccountRegistry.searchByPesel(data["pesel"])
    if check: 
        return jsonify({"message": "Account with this pesel already exists"}), 409
    else:
        account = PersonalAccount(data["name"], data["surname"], data["pesel"])
        AccountRegistry.addAcc(account)
        return jsonify({"message": "Account created"}), 201


@app.route("/api/accounts/count", methods=['GET'])
def count_accounts():
    count = AccountRegistry.countAcc()
    return jsonify({"Count": count}),200
    
@app.route("/api/accounts/<pesel>", methods=['GET'])
def get_account_by_pesel(pesel):
    account= AccountRegistry.searchByPesel(pesel)
    if account is None:
        return jsonify({"message": "Account not found"}), 404
    return jsonify({"name": account.name, "surname": account.surname,"balance": account.balance}), 201

@app.route("/api/accounts/<pesel>", methods=['PATCH'])
def update_account(pesel):
    data = request.get_json()
    account = AccountRegistry.updateAcc(pesel,data)
    if account is None:
        return jsonify({"message": "Account not found"}), 404
    return jsonify({
            "pesel": account.pesel,
            "name": account.name,
            "surname": account.surname,
        }), 200
    

@app.route("/api/accounts/<pesel>", methods=['DELETE'])
def delete_account(pesel):
    if AccountRegistry.removeAcc(pesel):
        return jsonify({"message": "Account deleted"}), 200
    else:
        return jsonify({"message": "Account not found"}), 404

@app.route("/api/accounts/<pesel>/transfer", methods=['POST'])
def transfers(pesel):
    data = request.get_json()
    account = AccountRegistry.searchByPesel(pesel)
    if account is None:
        return jsonify({"message": "Account not found"}), 404
    prev_balance = account.balance
    if data["type"] == "incoming":
        account.inTransfer(int(data["amount"]))
        if prev_balance != account.balance:
            return jsonify({"message": "the order has been accepted for execution", "balance": account.balance}), 200
        else:
            return jsonify({"message": "the order has NOT been accepted for execution"}), 422
    elif data["type"] == "outgoing":
        account.outTransfer(int(data["amount"]))
        if prev_balance != account.balance:
            return jsonify({"message": "the order has been accepted for execution", "balance": account.balance}), 200
        else:
            return jsonify({"message": "the order has NOT been accepted for execution"}), 422
    elif data["type"] == "express": 
        account.expressOutTransfer(int(data["amount"]))
        if prev_balance != account.balance:
            return jsonify({"message": "the order has been accepted for execution", "balance": account.balance}), 200
        else:
            return jsonify({"message": "the order has NOT been accepted for execution"}), 422
    else:
        return jsonify({"message": "Incorrect type of transfer", "balance": account.balance}), 400





