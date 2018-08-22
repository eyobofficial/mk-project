$(function(){
    // Subscription Form
    var subscriptionForm = $('#subscription-form');
    subscriptionForm.submit(function(event){
        event.preventDefault();
        $.ajax({
            url: "/subscribe/",
            data: {
                "csrfmiddlewaretoken": $('#subscription-form input[name=csrfmiddlewaretoken]').val(),
                "email": $('#reg-email').val()
            },
            type: 'POST',
            success: function(data){
                handleSubscribtion();
            },
            error: function(xhr, status, error){
                handleSubscribtion();
            }
        })
    });

    function handleSubscribtion(){
        $('#subscription-form-container').addClass('invisible');
        $('.subscription-feedback').removeClass('gone');
    }

    // Message Form
    var messageForm = $('#message_form');
    messageForm.submit(function(event){
        event.preventDefault();

        var nameInput = $('#mes-name');
        var emailInput = $('#mes-email');
        var messageInput = $('#mes-text');

        $.ajax({
            url: '/message/',
            type: 'POST',
            data: {
                "csrfmiddlewaretoken": $('#message_form input[name=csrfmiddlewaretoken]').val(),
                'name': $('#mes-name').val(),
                'email': $('#mes-email').val(),
                'message': $('#mes-text').val()
            },
            success: function(data){
                nameInput.val('');
                emailInput.val('');
                messageInput.val('');
                $('.form-text-feedback').removeClass('invisible');
            }
        })
    });
});