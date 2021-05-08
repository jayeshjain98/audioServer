def metadata_parser(data):
    try:
        metadata = data['audioMetadata']
        if data['audioFileType'] == 'Song':
            return 'Song',(metadata['song_id'].upper(),metadata['song_name'],metadata['song_duration'],metadata['song_upload_time'])
        
        elif data['audioFileType'] == 'Podcast':
            participants = metadata['participants']
            empty_list = ['','','','','','','','','','']
            participants.extend(empty_list[len(participants):])
            return 'Podcast',(metadata['podcast_id'].upper(), metadata['podcast_name'], metadata['host'], metadata['podcast_duration'], participants[0], participants[1], participants[2], participants[3], participants[4], participants[5], participants[6], participants[7], participants[8], participants[9], metadata['podcast_upload_time'])

        elif data['audioFileType'] == 'Audiobook':
            return 'Audiobook',(metadata['audiobook_id'].upper(), metadata['audiobook_title'], metadata['author'], metadata['narrator'], metadata['audiobook_duration'], metadata['audiobook_upload_time'])
    
    except Exception as error:
        raise error
