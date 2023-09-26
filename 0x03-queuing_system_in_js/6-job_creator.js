import { createQueue } from "kue";

const queue = createQueue({name: 'push_notification_code'});

const job_data = queue.create('push_notification_code',{
  phoneNumber: '+2347056839557',
  message: 'this is my whatsapp contact',
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