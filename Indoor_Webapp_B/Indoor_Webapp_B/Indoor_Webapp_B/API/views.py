from rest_framework import status, response, views


class HelloAPIView(views.APIView):

    def get(self, request):
        """
        The ``GET`` call will return a simple message.
        """
        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'detail': 'Hello World!',
            }
        )

        # Question and Answers:
        # QUESITON 1: Where do I lookup our status codes?
        # ANSWER 1: https://www.django-rest-framework.org/api-guide/status-codes/#status-codes

    def post(self, request):
        # Do not use the code below, this is what we used in ``Django``.
        data = request.POST  # Only handles form data.  Only works for 'POST' method.

        # This is how we get unvalidated data from the request.
        data = request.data  # Handles arbitrary data.  Works for 'POST', 'PUT' and 'PATCH' methods.

        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'detail': data,
            }
        )
