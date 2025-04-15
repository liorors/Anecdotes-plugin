from abc import ABC, abstractmethod

#abstract base class defining the plugin interface
class BasePlugin(ABC):
    @abstractmethod
    def login(self): pass  #perform connectivity/authentication check

    @abstractmethod
    def collect_user_details(self): pass  #Evidence E1

    @abstractmethod
    def collect_posts(self): pass  #Evidence E2

    @abstractmethod
    def collect_posts_with_comments(self): pass  #Evidence E3
