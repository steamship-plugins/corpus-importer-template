"""Example Steamship Importer Plugin.

An Importer is responsible for fetching data for import into the Steamship platform.
"""

from steamship.app import App, Response, post, create_handler
from steamship.plugin.corpus_importer import CorpusImporter, CorpusImportRequest, CorpusImportResponse
from steamship.plugin.service import PluginResponse, PluginRequest
from steamship.base.error import SteamshipError
from steamship.data.file import File


class CorpusImporterPlugin(CorpusImporter, App):
    """"Example Steamship Corpus Importer plugin."""

    def run(self, request: PluginRequest[CorpusImportRequest]) -> PluginResponse[CorpusImportResponse]:
        """Every plugin implements a `run` function.

        This template plugin does an extremely simple corpus import in which:
            - No matter what the user asked for..
            - We return a corpus import described by two fixed file import operations.
            - Each file import operation is hard-coded to a test File Importer in the Steamship Engine
        """

        if request is None:
            return Response(error=SteamshipError(message="Missing PluginRequest object."))

        if request.data is None:
            return Response(error=SteamshipError(message="Missing CorpusImportRequest object."))

        if request.data.fileImporterPluginInstance is None:
            return Response(error=SteamshipError(message="Missing associated fileImporterPluginInstance field."))

        # No matter what they asked for, return two hard coded files.
        r1 = File.CreateRequest(
            type="fileImporter", # E.g., as opposed to a direct file import
            pluginInstance=request.data.fileImporterPluginInstance
        )
        r2 = File.CreateRequest(
            type="fileImporter", # E.g., as opposed to a direct file import
            pluginInstance=request.data.fileImporterPluginInstance
        )

        return PluginResponse(data=CorpusImportResponse(
            fileImportRequests=[r1, r2]
        ))

    # Note: the path can diverge from the method name, as below.
    @post('/import_corpus')
    def import_corpus(self, **kwargs) -> Response:
        """App endpoint for our plugin.

        The `run` method above implements the Plugin interface for a File Importer.
        This `/import_corpus` method exposes it over an HTTP endpoint as a Steamship App.

        When developing your own plugin, you can almost always leave the below code unchanged.
        """
        request = CorpusImporter.parse_request(request=kwargs)
        response = self.run(request)
        return CorpusImporter.response_to_dict(response)


handler = create_handler(CorpusImporterPlugin)
