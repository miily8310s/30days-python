import os

# __file__は今開いているファイルの絶対パス（python3.9〜）
# 相対パスで指定→相対パスが返す、絶対パスで指定→絶対パス（〜python3.8）
FILE_PATH = os.path.abspath(__file__)
# dirnameで指定したファイルのフォルダ名だけを取得
BASE_DIR = os.path.dirname(FILE_PATH)
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

class Template:
  template_name = ""
  context = None

  def __init__(self, template_name='', context=None, *arg, **kwargs):
    self.template_name = template_name
    self.context = context
  
  def get_template(self):
    template_path = os.path.join(TEMPLATE_DIR, self.template_name)
    if not os.path.exists(template_path):
      raise Exception("This path does not exist")
    template_string = ''
    # withで囲うと自動的にファイルがクローズされる
    with open(template_path, 'r') as f:
      # readメソッド：開いたファイル全体を文字列として取得
      template_string = f.read()
    return template_string

  def render(self, context=None):
    render_ctx = context
    if self.context != None:
      render_ctx = self.context
    # dict: {dd: "test1", ee: "test2"}な型
    if not isinstance(render_ctx, dict):
      render_ctx = {}
    template_string = self.get_template()
    return template_string.format(**render_ctx)