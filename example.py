from ssftw import SSFTW

# Pass the ssdeep executable path to the class constructor.
ssdeep = SSFTW("C:\\ssdeep-2.13\\ssdeep.exe")

print "[+] Computing hashes from 2 files."
# Computing hash from files
hash1 = ssdeep.hash_from_file("C:\\Users\\user\\Desktop\\file1.exe")
hash2 = ssdeep.hash_from_file("C:\\Users\\user\\Desktop\\file2.exe")
print "Hash 1:%s\nHash 2:%s" % (hash1, hash2)

# Comparing two hashes
print "Ratio: %d" % ssdeep.compare(hash1, hash2)

print "--" * 30

print "[+] Computing hashes from 2 strings."
# Computing hash from files
hash1 = ssdeep.hash("Some long string, man.")
hash2 = ssdeep.hash("Similar long string, man!")
print "Hash 1:%s\nHash 2:%s" % (hash1, hash2)

# Comparing two hashes
print "Ratio: %d" % ssdeep.compare(hash1, hash2)
