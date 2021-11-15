msg_template = """Hello {name},
Thank you for joining {website}. We are very
happy to have you with us.
""" 

def format_msg(my_name='Justin', my_website='cfe.sh'):
  return msg_template.format(name=my_name, website=my_website)