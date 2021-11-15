import imaplib
import email

host = 'imap.gmail.com'
username = 'hungrypy@gmail.com'
password = '<your password>'

def get_inbox():
  mail = imaplib.IMAP4_SSL(host)
  mail.login(username, password)
  # メールボックスを選択
  mail.select('inbox')
  # 'UNSEEN'（未読）のメールを検索
  _, search_data = mail.search(None, 'UNSEEN')
  my_message = []
  # 
  for num in search_data[0].split():
    email_data = {}
    # '(RFC822)'が入ったメッセージのデータを取り出す
    _, data = mail.fetch(num, '(RFC822)')
    _, b = data[0]
    # fetchメソッドで1番めに引っかかったメールからメッセージオブジェクトを取得
    email_message = email.message_from_bytes(b)
    for header in ['subject', 'to', 'from', 'date']:
        print("{}: {}".format(header, email_message[header]))
        email_data[header] = email_message[header]
    # メッセージオブジェクトのプロパティを1つforループで回す
    for part in email_message.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
            email_data['body'] = body.decode()
        elif part.get_content_type() == "text/html":
            html_body = part.get_payload(decode=True)
            email_data['html_body'] = html_body.decode()
    my_message.append(email_data)
  return my_message

if __name__ == "__main__":
  print(get_inbox())