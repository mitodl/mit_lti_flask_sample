from orator.migrations import Migration


class CreateLtiSessionTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('ltiSessions') as table:
            table.increments('id')
            table.timestamps()
            table.string('custom_exercise')
            table.string('oauth_consumer_key')
            table.string('launch_presentation_return_url')
            table.string('user_id')
            table.string('oauth_nonce')
            table.string('context_label').nullable()
            table.string('context_id')
            table.string('resource_link_title').nullable()
            table.string('resource_link_id')
            table.string('lti_authenticated').nullable()
            table.string('lis_person_contact_email_primary').nullable()
            table.string('lis_person_contact_emailprimary').nullable()
            table.string('lis_person_name_full').nullable()
            table.string('lis_person_name_family').nullable()
            table.string('lis_person_name_given').nullable()
            table.string('lis_result_sourcedid')
            table.string('lis_person_sourcedid').nullable()
            table.string('launch_type').nullable()
            table.string('lti_message').nullable()
            table.string('lti_version').nullable()
            table.string('roles')
            table.string('lis_outcome_service_url').nullable()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('ltiSessions')
