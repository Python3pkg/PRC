################################################################################
############################## Classes #########################################
################################################################################
class PRCException(Exception): pass
class PRCCmd(str): pass

################################################################################
############################## Commands ########################################
################################################################################
PRC_NEW_SESSION = PRCCmd("PRC_NEW_SESSION")
PRC_EXIT = PRCCmd("PRC_EXIT")
PRC_OUTPUT = PRCCmd("PRC_OUTPUT")
PRC_CONFIRM = PRCCmd("PRC_CONFIRM")
PRC_PROMPT = PRCCmd("PRC_PROMPT")
PRC_CODE = PRCCmd("PRC_CODE")

################################################################################
############################## Constants #######################################
################################################################################

DEFAULT_PORT = 49988