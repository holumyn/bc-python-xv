class NotesApplication(object):
    
    def __init__(self,author):
        self.author = author
        self.notes_list  = []
        
        
    def create(self, note_content):
        return self.notes_list.append(note_content)

    def list(self):
        for idx,ls in enumerate(self.notes_list):
            print("Note ID: %d \n %s \nBy Author %s" % (idx, ls, self.author))
            
    def get(self, note_id):
        return "%s" % (self.notes_list[note_id])

    def search(self, search_text):
        print(any(search_text in item for item in self.notes_list))

    def delete(self, note_id):
        return self.notes_list.pop(note_id) 
        

    def edit(self, note_id, new_content):
        self.notes_list[note_id] = new_content
        return self.notes_list


