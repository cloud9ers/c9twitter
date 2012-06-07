APP_ROOT = '/crawler'

def router(map):
    #map.connect('master', '/{controller}/{action}') # master app example
    with map.submapper(path_prefix=APP_ROOT) as m:
#        m.connect("home", "/", controller="main", action="index")
        m.connect(None, "/", controller='C9Twitter', action='search')
        # ADD CUSTOM ROUTES HERE
        #m.connect(None, "/error/{action}/{id}", controller="error")
