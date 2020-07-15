from flask import Flask, jsonify, abort, request, make_response

app = Flask(__name__)

@app.route('/eligibles', methods = ['GET'])
def eligible_api():
    email = request.args.get('email_address')
    employee_id = request.args.get('employee_id')
    document = request.args.get('document')

    if email is None and employee_id is None and document is None:
        return make_response(
          error_message_format("param.none_given"), 400
        )
    fake_email = "teste@teste.company.com"
    fake_employee_id = "abc123"
    fake_document = "1234567890"

    if email != fake_email and employee_id != fake_employee_id and document != fake_document:
        return make_response(error_message_format("eligiblity.not_found"), 404)

    print(email)
    return jsonify(
      email_address = fake_email,
      employee_id = fake_employee_id,
      document = fake_document,
      company_id = 1
    )

@app.route('/register', methods = ['POST'])
def core_register():
    body = request.get_json()

    name = body.get("name")
    email = body.get("email_address")
    password = body.get("password")

    if name is None or email is None or password is None:
        return make_response(error_message_format("params.some_missing"), 400)

    if email == "used-email@email.com":
        return make_response(error_message_format("params.email_already_used"), 400)

    new_user_resp = jsonify(id = 1, name = name, email = email)

    return make_response(new_user_resp, 201)

@app.route('/associate', methods = ['POST'])
def core_asssociate():
    body = request.get_json()

    print(body)

    email = body.get("email_address")
    company_member_token = body.get("company_member_token")
    personal_document = body.get("personal_document")
    company_id = body.get("company_id")

    if (email is None and company_member_token is None and personal_document is None):
        return make_response(error_message_format("param.none_given"), 400)

    if company_id is None:
        return make_response(error_message_format("params.company_id_missing"), 400)

    if company_id == 1:
        if email is None:
            return make_response(error_message_format("params.email_missing"), 400)
        email_and_domain = email.split("@")
        if len(email_and_domain) != 2:
            return make_response(error_message_format("params.email_bad_format"), 400)
        domain = email_and_domain[1]

        if domain != "teste.company.com":
            return make_response(error_message_format("params.invalid_domain"), 400)
        return make_response(
          jsonify({
            "company_member": {
              "id": 1,
              "person_id": 1,
              "company_id": 1
            }
          })
        )

    if company_id == 2:
      if company_member_token is None or personal_document is None:
            return make_response(error_message_format("params.some_missing"), 400)
      if company_member_token != "abc123" or personal_document != "1234567890":
          return make_response(error_message_format("association.not_possible_to_associate"), 400)
      return make_response(
        jsonify({
            "company_member": {
              "id": 1,
              "person_id": 1,
              "company_id": 2
            }
          })
      )

@app.route('/company-members', methods = ['GET'])
def core_company_members():
    email = request.args.get('email_address')
    company_member_token = request.args.get('company_member_token')
    cpf = request.args.get('personal_document')

    if email is None and company_member_token is None and cpf is None:
        return make_response(
          error_message_format("param.none_given"), 400
        )

    fake_email = "teste@teste.company.com"
    fake_company_member_token = "abc123"
    fake_cpf = "1234567890"

    if email != fake_email and company_member_token != fake_company_member_token and fake_cpf != cpf:
        return make_response(error_message_format("company_member.not_found"), 404)

    return jsonify(
      email_address = fake_email,
      token = fake_company_member_token,
      cpf = fake_cpf,
      company_id = 1
    )

def error_message_format(key):
    return jsonify({
      "error" : {
        "message": "random message",
        "key": key
      }
    })

if __name__ == "__main__":
    app.run(port=3001)
