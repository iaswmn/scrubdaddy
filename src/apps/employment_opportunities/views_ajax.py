import tempfile

from django.views.generic.base import View

from libs.upload import upload_chunked_file, TemporaryFileNotFoundError, NotLastChunk
from libs.views_ajax import AjaxViewMixin


class UploadView(AjaxViewMixin, View):
    def post(self, request):
        try:
            uploaded_file = upload_chunked_file(request, 'images')
        except TemporaryFileNotFoundError as e:
            return self.json_error({
                'message': str(e),
            })
        except NotLastChunk:
            return self.json_response()

        tmp_file = tempfile.NamedTemporaryFile(delete=False)
        for chunk in uploaded_file.chunks():
            tmp_file.write(chunk)
        uploaded_file.close()

        return self.json_response({
            'name': uploaded_file.name,
            'filename': tmp_file.name,
        })