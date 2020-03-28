import os
import requests
import json
import time

def grouper(seq, size):
        return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def communicate(input_sequence, file_name):
        submit = 'http://bioinf.cs.ucl.ac.uk/psipred/api/submission.json'

        payload = {'input_data': ('input.txt', input_sequence)}
        data = {'job': 'psipred',
                'submission_name': 'test',
                'email': 'dummy@dummy.com', }
        r = requests.post(submit, data=data, files=payload)

        parsed = json.loads(r.text)
        #print(json.dumps(parsed, indent=4, sort_keys=True))

        try:
                uuid = parsed['UUID']
        except:
                print(file_name+":" , parsed['error']['input_data'][0]+". Input might be too short.")
                return
        print("UUID: ", uuid)

        time.sleep(60)
        status = "Running"

        while(status == "Running"):
                complete = 'http://bioinf.cs.ucl.ac.uk/psipred/api/submission/' + uuid + '.json'

                r = requests.get(complete)
                parsed = json.loads(r.text)
                #print(json.dumps(parsed, indent=4, sort_keys=True))

                status = parsed['state']
                print("Status:",status)

        time.sleep(60)

        data_path = parsed['submissions'][0]['results'][5]['data_path']

        download = 'http://bioinf.cs.ucl.ac.uk/psipred/api' + data_path

        r = requests.get(download, allow_redirects=True)
        open(file_name + ".ss2", 'wb').write(r.content)
        print("Protein sequence stored in " + file_name + ".ss2")
        return

def main():
        '''Open input.txt and read line by line 
        the first line is the protein name and 
        the second line is the protein sequence''' 
        lines = [line.rstrip('\n') for line in open('input.txt')]
        groups = grouper(lines, 2)
        for group in groups:
                communicate(group[1], group[0])
                
if __name__ == "__main__":
        main()