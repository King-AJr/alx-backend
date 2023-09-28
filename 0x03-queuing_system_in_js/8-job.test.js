const { expect } = require('chai');
const kue = require('kue');
const createPushNotificationsJobs = require('./8-job.js'); // Replace with the actual module path

// Create a test queue
const testQueue = kue.createQueue({
  redis: {
    port: 6379, // Replace with your Redis server port
    host: 'localhost', // Replace with your Redis server host
  },
});

describe('createPushNotificationsJobs', () => {
  before(() => {
    // Enter test mode without processing jobs
    testQueue.testMode.enter();
  });

  after(() => {
    // Clear the queue and exit test mode
    testQueue.testMode.exit();
  });

  it('should add jobs to the queue', () => {
    const jobs = [
      { title: 'Job 1', message: 'Message 1' },
      { title: 'Job 2', message: 'Message 2' },
    ];

    createPushNotificationsJobs(jobs, testQueue);

    // Check if the jobs were enqueued
    expect(testQueue.testMode.jobs.length).to.equal(jobs.length);
  });

  it('should throw an error for non-array input', () => {
    const invalidJobs = 'Not an array';

    // Using a function inside an assertion to catch the error
    expect(() => createPushNotificationsJobs(invalidJobs, testQueue)).to.throw('Jobs is not an array');
  });


  it('should emit events when jobs are processed', (done) => {
    const jobInfo = { title: 'Job 3', message: 'Message 3' };
  
    const job = testQueue.create('push_notification_code_3', jobInfo);
  
    // Listen for job events
    job.on('enqueue', () => {
      console.log('Job enqueued');
    }).on('complete', () => {
      console.log('Job completed');
      done(); // Signal that the test is done
    }).on('failed', (err) => {
      console.error('Job failed:', err);
      done(err); // Signal that the test is done with an error if the job fails
    });
  
    // Save the job to trigger the events
    job.save();
  });
  
});
