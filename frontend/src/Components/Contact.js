
const Contact = () => {
    return ( 
        <section className="contact container" id="contact">
            <h2 className="heading">Contact</h2>

            <form action="" className="contact-form" id="contact-form">
                <input type="text" placeholder="Your Name" className="name" required/>
                <input type="email" name="" id="" placeholder="Your Email" className="email" required/>
                <textarea name="" id="" cols="30" rows="10" placeholder="Write message here..." className="message"></textarea>
                <input type="submit" value="send" className="send-btn" />
            </form>
        </section>
     );
}
 
export default Contact;