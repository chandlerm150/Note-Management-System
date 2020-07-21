class callNote:
  def __init__(self, sID, forWho, reason, notes, empID):
        self.sID = int(sID)
        self.reason = reason
        self.note = notes
        self.forWho = forWho
        self.eID = int(empID)
        self.createdDate = ""
        self.status = 0
        self.noteID = 0

