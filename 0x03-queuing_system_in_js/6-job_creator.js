import { createQueue } from "kue";

const queue = createQueue();

const job_data = queue.create('push_notification_code',{
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
});

//created without error
job_data.on('enqueue', () => {
  console.log(`Notification job created: ${job_data.id}`)
})
.on('complete', () => {
  console.log('Notification job completed')
})
.on('failed', () => {
  console.error('Notification job failed')
});
job_data.save()