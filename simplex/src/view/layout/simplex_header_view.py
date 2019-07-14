class SimplexHeader():
    def __init__(self):
        self.classes = []
        self.icons = []

    def render(self):
        header = """
        <div class="simplex-main-menu">
          <div class="icon">
            <h2 class="simplex-main-menu-title">
              <a href="{{ url_for('index') }}">Simplex</a>
            </h2>
          </div>
          <div class="simplex-user-menu">
              <i class="item fas fa-user"></i>
              <i class="item fas fa-envelope"></i>
          </div>
        </div>
        """
        return header
