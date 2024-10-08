def validate_and_extract_log(s):
# Function that extracts and validates manufacturing logs
# Input : Log string
# Output : List of dicts and a flag indicating valid/invalid

#Set a validity flag, 1 for valid and 0 for invalid
    valid = 0
    batch_chk = 0
    prod_chk = 0
    qty_chk = 0
    date_chk = 0
    output = []

    while(len(s)>0):
        #Check if string is empty or null
        if (s == "" or s == None):
            valid = 0

        #Extract batch
        if (s[0] == 'B' and s[1:5].isdecimal()):
            batch_chk = 1
            batch_id = s[1:5]
        else:
            batch_chk = 0

        #Extract product
        s = s[5:]
        if (batch_chk == 1 and (s[0] == 'P') and (s[1:3].isupper()) and s[1:3].isalpha()):
            prod_chk = 1
            prod_code = s[1:3]
        else:
            prod_chk = 0

        #Extract qty
        s = s[3:]
        if (prod_chk == 1 and s[0]=='Q' and s[1:s.index('D')].isdecimal()):
            qty_chk = 1
            qty = int(s[1:s.index('D')])
        else:
            qty_chk = 0

        #Extract date
        s = s[s.index('D'):]
        if (qty_chk == 1 and s[1:9].isdecimal() and (
                int(s[1:5]) >= 2000 and int(
                s[1:5]) <= 2099) and (
                int(s[5:7]) >= 1 and int(s[5:7]) <= 12) and (
                int(s[7:9]) >= 1 and int(s[7:9]) <= 31)):
             date_chk = 1
             year = s[1:5]
             mth = s[s.index('D')+5:s.index('D')+7]
             dd = s[s.index('D')+7:s.index('D')+9]
             date = year+mth+dd
        else:
            date_chk = 0

        if date_chk == 1:
            valid = 1
        else:
            valid = 0

        if valid == 1:
            # Build output
            dict = {
                "Batch ID": batch_id,
                "Product Code": prod_code,
                "Quantity": qty,
                "Date": date
            }
            output = output + [dict]

            # Check for new appended batches
            s = s[9:]

        else:
            return 'Invalid'

    if valid == 1:
        return output
    else:
        return 'Invalid'
