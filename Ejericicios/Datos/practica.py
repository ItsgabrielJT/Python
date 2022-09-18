class MySeq:
  def __init__( self , seq, seq_type = "DNA"):
    self.seq = seq
    self.seq_type = seq_type
  def print_sequence( self ):
    print ("Sequence: " + self .seq)
  def get_seq_biotype ( self ):
    return self .seq_type
  def show_info_seq ( self ):
    print ("Sequence: " + self .seq + " biotype: " + self .seq_type)
  def count_occurrences( self , seq_search):
    return self .seq.count(seq_search)
  def set_seq_biotype (self , bt):
      biotype = bt.upper()
      if biotype == "DNA" or biotype == "RNA" or biotype == "PROTEIN":
          self.seq_type = biotype
      else:
        print ("Non biological sequence type!")

s1 = MySeq("ATAATGATAGATAGATGAT")
# access attribute values
print (s1.seq)
print (s1.seq_type)
s1.print_sequence()
print (s1.get_seq_biotype())

# the type of the sequence is updated to an invalid biotype
# by direct alteration of the attribute
s1.seq_type = "DNA"
# safer alternative: class method to validate update
    
# testing the update of the attribute
s1.set_seq_biotype("time series")
s1.set_seq_biotype("dna")
