import warnings

warnings.simplefilter("ignore", SyntaxWarning)
warnings.simplefilter("always", ImportWarning)


warnings.warn("Warning! No code here", SyntaxWarning)
warnings.warn("Warning! Module not import", ImportWarning)

