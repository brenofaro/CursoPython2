from log import LogFileMixin, LogPrintMixin

lp = LogPrintMixin()
lp._log("Qualquer")
lp.log_error("Envio")

lf = LogFileMixin()
lf._log("Qualquer")
lf.log_error("Envio")