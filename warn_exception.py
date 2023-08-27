#Також варто пам’ятати, що обробити попередження конструкцією try-except вдасться,
# лише якщо фільтр встановлено в положення error
import warnings

warnings.simplefilter("ignore", SyntaxWarning)
warnings.simplefilter("error", ImportWarning)

warnings.warn("Warning! No code here", SyntaxWarning)
try:
    warnings.warn("Warning! Module not import", ImportWarning)
except:
    print("Warning processed")