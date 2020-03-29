import _sqlite3
from .passwordHasher import hash_password
conn = _sqlite3.connect('shopBase.db')

c = conn.cursor()

def registerUser(last_name, first_name, postcode, street, house_number, password,email):
    """regestier a user into database hash password !! and return true when success else false"""
    sql = """ INSERT INTO user (email, last_name, firstname,postcode, street, house_number, password) VALUES ('{}','{}','{}',{},'{}','{}','{}')"""
    hashedPw = hash_password(password)
    success = True
    try:
        with conn:
            sqlFor = sql.format(email, last_name, first_name, postcode, street, house_number, hashedPw)
            print(sqlFor)
            c.execute(sqlFor)
    except:
        success = False

    return success

def getUserfromSessionID(sessionID):
    """ a function to help find the user_id from the sessionID folder"""
    sql = """ SELECT user_id FROM session WHERE session_id = '{}'"""
    result = None
    try:
        with conn:
            sqlFor = sql.format(sessionID)
            print(sqlFor)
            c.execute(sqlFor)
            result = c.fetchone()
    except:
        result = -1

    return result

def login(email, password):
    """ check if user is in database if in db generate sesid and insert into db  return sessid if success else -1"""
    pass

def logout(sessionID):
    """ remove sesID from db return true if success else false"""
    pass

def getArtikels():
    """return all articels as a List with dictonary {id:, name:}"""
    pass

def getAuftraege(sessionId,plz):
    """check if plz is -1 if -1 return all auftraege assoziated with that user else all auftrege in that plz  return type: list with dictonary {errandid, postcode} else -1"""
    pass

def getAuftrag(sessionid,auftragid):
    """get all the information from that errand as a dictonary"""
    pass

def takeErrand(sessionID, errandID):
    """in db add to user_accepted_errand if errend isnt taken (status = 0), change status from errand to one  return true or false """
    pass

def makeErrand(postcode,email, phone_number, notice, articleList):
    """ create an new errand with the informathion status default is 0 / articleList looks like that [{item_id, amount}] add to errand and the from article list in items_in_errand  return bool for success"""