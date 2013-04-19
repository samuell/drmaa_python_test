#
# Simple test script to run a short job
#
import os, drmaa

# Create a session
s = drmaa.Session()
s.initialize()

# Create a Job Template
jt = s.createJobTemplate()
jt.remoteCommand = os.getcwd() + "/sleeper.sh"
jt.nativeSpecification = '-A staff -p core -n 1 --qos=short'

# Run the job
jobid = s.runJob(jt)
print "Started job with id %s!" % jobid

# Check status
jobstatus = s.jobStatus(jobid)
print "Job status is now: %s" % jobstatus

# Cancel the job
s.control(jobid, drmaa.JobControlAction.TERMINATE)
print "Trying to cancel the job ..."

# Check job status again
jobstatus = s.jobStatus(jobid)
print "Job status is now: %s" % jobstatus
print "Script finished!"
