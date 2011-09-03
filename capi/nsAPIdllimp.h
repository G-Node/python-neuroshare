///////////////////////////////////////////////////////////////////////////////////////////////////
//
// Copyright (C) 2003  Neuroshare Project                                                         
//
// This library is free software; you can redistribute it and/or
// modify it under the terms of the GNU Lesser General Public
// License as published by the Free Software Foundation; either
// version 2.1 of the License, or (at your option) any later version.
//
// This library is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
// Lesser General Public License for more details.
//
// A copy of the GNU Lesser General Public License can be obtained by writing to:
//  Free Software Foundation, Inc.,
//  59 Temple Place, Suite 330,
//  Boston, MA  02111-1307
//  USA
//
// Contact information:
//  Angela Wang
//  CyberKinetics, Inc.,
//  391 G Chipeta Way
//  Salt Lake City,  UT  84108
//  USA
//  angela@bionictech.com
//
// Website:
//  www.neuroshare.org
//
// All other copyrights on this material are replaced by this license agreeement.
//
///////////////////////////////////////////////////////////////////////////////////////////////////
/* $Workfile: nsAPIdllimp.h $
*/
//
// File version  : 1.0
//
// Specification : based on Neuroshare API specification version 1.0
//
// Description   : This header file contains Neuroshare API function prototype delarations in 
//                 pointer form for importing Neuroshare function definitions from a DLL.
//                 The file nsAPIdllimp.c contains C code to declare and load the functions.
//
// Authors       : Shane Guillory, Angela Wang
//
/* $Date: 2/21/03 12:42p $
*/
//
/* $History: nsAPIdllimp.h $
// 
// *****************  Version 9  *****************
// User: Almut        Date: 2/21/03    Time: 12:42p
// Updated in $/Neuroshare/DLLTester
// These headers now conform to Neuroshare API Spec 1.0
// 
// *****************  Version 1  *****************
// User: Angela       Date: 2/21/03    Time: 11:45a
// Created in $/Neuroshare/nsNEVLibrary
// Version 1.0 Neuroshare Specifications
// 
// *****************  Version 1  *****************
// User: Angela       Date: 2/17/03    Time: 11:22a
// Created in $/Neuroshare/nsNEVLibrary
// Neuroshare API Ver 1.0 compliant header files
// 
// *****************  Version 1  *****************
// User: Angela       Date: 2/13/03    Time: 9:29a
// Created in $/Neuroshare/nsNEVLibrary
 * 
 * *****************  Version 8  *****************
 * User: Angela       Date: 1/14/03    Time: 9:44a
 * Updated in $/Neuroshare/nsNEVLibrary
 * 
 * *****************  Version 7  *****************
 * User: Angela       Date: 1/10/03    Time: 12:15p
 * Updated in $/Neuroshare/nsNEVLibrary
 * Reword disclaimer
 * 
 * *****************  Version 6  *****************
 * User: Angela       Date: 1/09/03    Time: 12:13p
 * Updated in $/Neuroshare/nsNEVLibrary
 * Changed some formatting of headers to look nicer
 * 
 * *****************  Version 5  *****************
 * User: Angela       Date: 1/09/03    Time: 11:55a
 * Updated in $/Neuroshare/nsNEVLibrary
 * Added file headers, copyright, function headers

    v0.9b - Functions changed to use __stdcall calling convention for compatibility 
        with Visual Basic. Function prototype declarations also changed to
        all-capital versions of the neuroshare function names.
    v0.9b - First public release.. 
*/
///////////////////////////////////////////////////////////////////////////////////////////////////


// Standard include guards
#ifndef NSAPIDLLIMP_H_INCLUDED
#define NSAPIDLLIMP_H_INCLUDED

#include "nsAPItypes.h"


// Only need to specify "C" naming convention if using mixed C/C++
// It won't hurt if all C or all C++, so let's be safe
#ifdef __cplusplus
extern "C" 
{
#endif

#ifndef _WIN32
#define __stdcall
#endif


///////////////////////////////////////////////////////////////////////////////////////////////////
//
//          Definitions of function pointers
//
///////////////////////////////////////////////////////////////////////////////////////////////////



///////////////////////////////////////////////////////////////////////////////////////////////////
// Define pointer to ns_GetLibraryInfo
//  
// Purpose:
//	Retrieves information about the loaded API library
//
// Parameters:
//	ns_LIBRARYINFO *pLibraryInfo	pointer to ns_LIBRARYINFO structure to receive information 
//	uint32 dwLibraryInfoSize		size in bytes of ns_LIBRARYINFO structure
//
// Return Values:
//	ns_OK							ns_LIBIRARYINFO successfully retrieved
//	ns_LIBEERROR					library error
//
///////////////////////////////////////////////////////////////////////////////////////////////////

typedef ns_RESULT (__stdcall *NS_GETLIBRARYINFO) 
    (ns_LIBRARYINFO *pLibraryInfo, uint32 dwLibraryInfoSize);



///////////////////////////////////////////////////////////////////////////////////////////////////
// Define pointer to ns_OpenFile
//  
// Purpose:
//	Opens the data file and assigns a file handle for internal use by the library.
//
// Parameters:
//	char *pszFilename	name of file to open
//	uint32 *hFile		pointer to a file handle
//
// Return Values:
//	ns_OK				ns_LIBIRARYINFO successfully retrieved
//	ns_TYPEERROR		library unable to open file type
//	ns_FILEERROR		file access or read error 
//	ns_LIBEERROR		library error
//
///////////////////////////////////////////////////////////////////////////////////////////////////

typedef ns_RESULT (__stdcall *NS_OPENFILE)
	(const char *pszFilename, uint32 *hFile);



///////////////////////////////////////////////////////////////////////////////////////////////////
// Define pointer to ns_GetFileInfo
//  
// Purpose:
//	Retrieve general information about the data file
//
// Parameters:
//	uint32 hFile				handle to NEV data file
//	ns_FILEINFO *pFileInfo		pointer to ns_FILEINFO structure that receives data
//	uint32 dwFileInfoSize		number of bytes returned in ns_FILEINFO
//
// Return Values:
//	ns_OK						function succeeded
//	ns_BADFILE					invalid file handle
//	ns_FILEERROR				file access or read error
//	ns_LIBERROR					library error, null pointer
//
///////////////////////////////////////////////////////////////////////////////////////////////////

typedef ns_RESULT (__stdcall *NS_GETFILEINFO)	
	(uint32 hFile, ns_FILEINFO *pFileInfo, uint32 dwFileInfoSize);



///////////////////////////////////////////////////////////////////////////////////////////////////
// Define pointer to ns_CloseFile
//  
// Purpose:
//	Close the open data file
//
// Parameters:
//	uint32 hFile				handle to NEV data file
//
// Return Values:
//	ns_OK						function succeeded
//	ns_BADFILE					invalid file handle
//	
///////////////////////////////////////////////////////////////////////////////////////////////////

typedef ns_RESULT (__stdcall *NS_CLOSEFILE)	
	(uint32 hFile);



///////////////////////////////////////////////////////////////////////////////////////////////////
// Define pointer to ns_GetEntityInfo
//  
// Purpose:
//	Retrieve Entity information
//
// Parameters:
//	uint32 hFile				handle to NEV data file
//	uint32 dwEntityID			entity ID
//	ns_ENTITYINFO *pEntityInfo	pointer to ns_ENTITYINFO structure that receives information 
//	uint32 dwEntityInfoSize		number of bytes returned in ns_ENTITYINFO
//
// Return Values:
//	ns_OK						function succeeded
//	ns_BADFILE					invalid file handle
//	ns_LIBERROR					library error, null pointer
//
///////////////////////////////////////////////////////////////////////////////////////////////////

typedef ns_RESULT (__stdcall *NS_GETENTITYINFO)
	(uint32 hFile, uint32 dwEntityID, ns_ENTITYINFO *pEntityInfo, uint32 dwEntityInfoSize);



///////////////////////////////////////////////////////////////////////////////////////////////////
// Define pointer to ns_GetEventInfo
//  
// Purpose:
//	Retrieve information for Event entities.
//
// Parameters:
//	uint32 hFile				handle to NEV data file
//	uint32 dwEntityID			Event entity ID
//	ns_EVENTINFO *pEventInfo	pointer to ns_EVENTINFO structure to receive information 
//	uint32 dwEventInfoSize		number of bytes returned in ns_EVENTINFO
//
// Return Values:
//	ns_OK						function succeeded
//	ns_BADFILE					invalid file handle
//  ns_BADENTITY				inappropriate or invalid entity identifier
//	ns_LIBERROR					library error, null pointer
//
///////////////////////////////////////////////////////////////////////////////////////////////////

typedef ns_RESULT (__stdcall *NS_GETEVENTINFO)
	(uint32 hFile, uint32 dwEntityID, ns_EVENTINFO *pEventInfo, uint32 dwEventInfoSize);



///////////////////////////////////////////////////////////////////////////////////////////////////
// Define pointer to ns_GetEventData
//  
// Purpose:
//	Retrieve the timestamp and Evevy entity data items.
//
// Parameters:
//	uint32 hFile				handle to NEV data file
//	uint32 dwEntityID			Event entity ID
//	uint32 nIndex				Event entity item number
//	double *pdTimeStamp			pointer to double timestamp (in seconds)
//	void   *pData				pointer to data buffer to receive data
//	uint32 *pdwDataSize			pointer to number of bytes of data retrieved into data buffer
//
// Return Values:
//	ns_OK						function succeeded
//	ns_BADFILE					invalid file handle
//  ns_BADENTITY				inappropriate or invalie entity identifier
//	ns_LIBERROR					library error, null pointer
//
///////////////////////////////////////////////////////////////////////////////////////////////////

typedef ns_RESULT (__stdcall *NS_GETEVENTDATA)
	(uint32 hFile, uint32 dwEntityID, uint32 nIndex, double *pdTimeStamp, void *pData,
	 uint32 dwDataSize, uint32 *pdwDataRetSize);


///////////////////////////////////////////////////////////////////////////////////////////////////
// Define pointer to ns_GetAnalogInfo
// Purpose:
//
//	Retrieve information for Analog entities
// Parameters:
//
//	uint32 hFile				handle to NEV data file
//	uint32 dwEntityID			Analog entity ID
//	ns_ANALOGINFO *pAnalogInfo	pointer to ns_ANALOGINFO structure to receive data 
//	uint32 dwAnalogInfoSize		number of bytes returned in ns_ANALOGINFO
//
// Return Values:
//	ns_OK						function succeeded
//	ns_BADFILE					invalid file handle
//  ns_BADENTITY				inappropriate or invalie entity identifier
//	ns_LIBERROR					library error, null pointer
//
///////////////////////////////////////////////////////////////////////////////////////////////////

typedef ns_RESULT (__stdcall *NS_GETANALOGINFO)
	(uint32 hFile, uint32 dwEntityID, ns_ANALOGINFO *pAnalogInfo,uint32 dwAnalogInfoSize);



///////////////////////////////////////////////////////////////////////////////////////////////////
// Define pointer to ns_GetAnalogData
//  
// Purpose:
//	Retrieve analog data in the buffer at pData.  If possible, dwIndexCount, analog data values are
//	returned in the buffer.  As there may be time gaps in the sequential values, the number of
//	continuously sampled data items is returned in pdwContCount.
//
// Parameters:
//	uint32 hFile			handle to NEV data file
//	uint32 dwEntityID		Analog entity ID
//	uint32 dwStartIndex		starting index to search for timestamp
//	uint32 dwIndexCount		number of timestamps to retrieve
//	uint32 *pdwContCount	pointer to count of the first non-sequential analog item
//	double *pData			pointer of data buffer to receive data values
//
// Return Values:
//	ns_OK						function succeeded
//	ns_BADFILE					invalid file handle
//  ns_BADENTITY				inappropriate or invalid entity identifier
//	ns_LIBERROR					library error, null pointer
//
///////////////////////////////////////////////////////////////////////////////////////////////////

typedef ns_RESULT (__stdcall *NS_GETANALOGDATA)
	(uint32 hFile, uint32 dwEntityID, uint32 dwStartIndex, uint32 dwIndexCount, 
	 uint32 *pdwContCount, double *pData);



///////////////////////////////////////////////////////////////////////////////////////////////////
// Define pointer to ns_GetSegmentInfo
//  
// Purpose:
//	Retrieve information for Segment entities.
//
// Parameters:
//	uint32 hFile					handle to NEV data file
//	uint32 dwEntityID				Segment entity ID
//	ns_SEGMENTINFO *pSegmentInfo	pointer to ns_SEGMENTINFO structure to receive information
//	uint32 dwSegmentInfoSize		size in bytes retrieved in ns_SEGMENTINFO structure
//
// Return Values:
//	ns_OK							function succeeded
//	ns_BADFILE						invalid file handle
//	ns_BADENTITY					invalid or inappropriate entity identifier specified
//	ns_FILEERROR					file access or read error
//	ns_LIBERROR						library error
//
///////////////////////////////////////////////////////////////////////////////////////////////////

typedef ns_RESULT (__stdcall *NS_GETSEGMENTINFO)
	(uint32 hFile, uint32 dwEntityID, ns_SEGMENTINFO *pSegmentInfo,uint32 dwSegmentInfoSize);


///////////////////////////////////////////////////////////////////////////////////////////////////
// Define pointer to ns_GetSegmentSourceInfo
//  
// Purpose:
//	Retrieve information on the source, dwSourceID, generating segment entity dwEntityID.
//
// Parameters:
//	uint32 hFile					handle to NEV data file
//	uint32 dwEntityID				Segment entity ID
//	uint32 dwSourceID				entity ID of source
///	ns_SEGSOURCEINFO *pSourceInfo	pointer to ns_SEGSOURCEINFO structure to receive information
//	uint32 dwSourceInfoSize			size in bytes retrieved in ns_SEGSOURCEINFO structure
//
// Return Values:
//	ns_OK							function succeeded
//	ns_BADFILE						invalid file handle
//	ns_BADENTITY					invalid or inappropriate entity identifier specified
//	ns_FILEERROR					file access or read error
//	ns_LIBERROR						library error
//
///////////////////////////////////////////////////////////////////////////////////////////////////

typedef ns_RESULT (__stdcall *NS_GETSEGMENTSOURCEINFO)
	(uint32 hFile, uint32 dwEntityID, uint32 dwSourceID, ns_SEGSOURCEINFO *pSourceInfo,
	 uint32 dwSourceInfoSize);



///////////////////////////////////////////////////////////////////////////////////////////////////
// Define pointer to ns_GetSegmentData
//  
// Purpose:
//	Retrieve segment data waveform and its timestamp.
//	The number of data points read is returned at pdwSampleCount.
//
// Parameters:
//	uint32 hFile					handle to NEV data file
//	uint32 dwEntityID				Segment entity ID
//	int32 nIndex					Segment item index to retrieve
//	double *pdTimeStamp				pointer to timestamp to retrieve
//	double *pData					pointer to data buffer to receive data
//	uint32 *pdwSampleCount			pointer to number of data items retrieved 
//	uint32 *pdwUnitID				pointer to unit ID of Segment data
//
// Return Values:
//	ns_OK							function succeeded
//	ns_BADFILE						invalid file handle
//	ns_BADENTITY					invalid or inappropriate entity identifier specified
//	ns_FILEERROR					file access or read error
//	ns_LIBERROR						library error
//
///////////////////////////////////////////////////////////////////////////////////////////////////

typedef ns_RESULT (__stdcall *NS_GETSEGMENTDATA)
	(uint32 hFile, uint32 dwEntityID, int32 nIndex, double *pdTimeStamp, double *pdData,
   	 uint32 dwDataBufferSize, uint32 *pdwSampleCount, uint32 *pdwUnitID );



///////////////////////////////////////////////////////////////////////////////////////////////////
// Define pointer to ns_GetNeuralInfo
//  
// Purpose:
//	Retrieve information on Neural Events.
//
// Parameters:
//	uint32 hFile				handle to NEV data file
//	uint32 dwEntityID			Neural entity ID
//	ns_NEURALINFO *pNeuralInfo	pointer to ns_NEURALINFO structure to receive information 
//	uint32 dwNeuralInfoSize		number of bytes returned in ns_NEURALINFO
//
// Return Values:
//	ns_OK						function succeeded
//	ns_BADFILE					invalid file handle
//  ns_BADENTITY				inappropriate or invalid entity identifier
//	ns_LIBERROR					library error, null pointer
//
///////////////////////////////////////////////////////////////////////////////////////////////////


typedef ns_RESULT (__stdcall *NS_GETNEURALINFO)
	(uint32 hFile, uint32 dwEntityID, ns_NEURALINFO *pNeuralInfo, uint32 dwNeuralInfoSize);



///////////////////////////////////////////////////////////////////////////////////////////////////
// Define pointer to ns_GetNeuralData
//  
// Purpose:
//	Retrieve requested number of Neural event timestamps (in sec)
//
// Parameters:
//	uint32 hFile				handle to NEV data file
//	uint32 dwEntityID			Neural event entity ID
//	uint32 dwStartIndex			index of first Neural event item time to retrieve
//  uint32 dwIndexCount			number of Neural event items to retrieve
//	double *pData				pointer to buffer to receive times
//
// Return Values:
//	ns_OK						function succeeded
//	ns_BADFILE					invalid file handle
//  ns_BADENTITY				inappropriate or invalie entity identifier
//	ns_LIBERROR					library error, null pointer
//
///////////////////////////////////////////////////////////////////////////////////////////////////

typedef ns_RESULT (__stdcall *NS_GETNEURALDATA)
	(uint32 hFile, uint32 dwEntityID, uint32 dwStartIndex, uint32 dwIndexCount, double *pdData);



///////////////////////////////////////////////////////////////////////////////////////////////////
// Define pointer to ns_GetIndexByTime
//  
// Purpose:
//
//	Given the time (sec), return the closest data item index, as specified by nFlag.
//	Finds the packet with the closest time to the requested time.  
//
// Parameters:
//
//	uint32 hFile				handle to NEV data file
//	uint32 dwEntityID			entity ID to search for
//	uint32 dwSearchTimeStamp	timestamp of item to search for
//	int32 nFlag					position of item relative to the requested timestamp
//	uint32 *pdwIndex			pointer to index of item to retrieve 
//
// Return Values:
//
//	ns_OK						function succeeded
//	ns_BADFILE					invalid file handle
//	ns_LIBERROR					library error, null pointer
//
///////////////////////////////////////////////////////////////////////////////////////////////////

typedef ns_RESULT (__stdcall *NS_GETINDEXBYTIME)
	(uint32 hFile, uint32 dwEntityID, double dTime, int32 nFlag, uint32 *pdwIndex);



///////////////////////////////////////////////////////////////////////////////////////////////////
// Define pointer to ns_GetTimeByIndex
//  
// Purpose:
//
//	Given an index for an entity data item, return the time in seconds.
//
// Parameters:
//
//	uint32 hFile			handle to NEV data file
//	uint32 dwEntityID		entity ID to search for
//	uint32 dwIndex			index of entity item to search for
//	double *pdTime			time of entity to retrieve
//
// Return Values:
//
//	ns_OK						function succeeded
//	ns_BADFILE					invalid file handle
//	ns_LIBERROR					library error, null pointer
//
///////////////////////////////////////////////////////////////////////////////////////////////////

typedef ns_RESULT (__stdcall *NS_GETTIMEBYINDEX)
	(uint32 hFile, uint32 dwEntityID, uint32 dwIndex, double *pdTime);


///////////////////////////////////////////////////////////////////////////////////////////////////
// Define pointer to ns_GetLastErrorMsg
//  
// Purpose:  
//  Retrieve the most recent error text message
//
// Parameters:
//  char *pszMsgBuffer			pointer to text buffer to receive error message  
//  uint32 dwMsgBufferSize		size in bytes of text buffer
//
// Return Values:
//  ns_OK                       function succeeded
//  ns_LIBERROR                 library error
//
//
///////////////////////////////////////////////////////////////////////////////////////////////////

typedef ns_RESULT (__stdcall *NS_GETLASTERRORMSG)
	(char *pszMsgBuffer, uint32 dwMsgBufferSize);


//////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////
//  The names of the function pointers are defined here to standardize its use
//  in the application.
//
//  Function pointer variable names are defined in the host application.  If these
//  names are to be defined differently, this section should be commented out. 
//

#if 0
extern NS_GETLIBRARYINFO       ns_GetLibraryInfo;
extern NS_OPENFILE             ns_OpenFile;
extern NS_GETFILEINFO          ns_GetFileInfo;
extern NS_CLOSEFILE            ns_CloseFile;
extern NS_GETENTITYINFO        ns_GetEntityInfo;
extern NS_GETEVENTINFO         ns_GetEventInfo;
extern NS_GETEVENTDATA         ns_GetEventData;
extern NS_GETANALOGINFO        ns_GetAnalogInfo;
extern NS_GETANALOGDATA        ns_GetAnalogData;
extern NS_GETSEGMENTINFO       ns_GetSegmentInfo;
extern NS_GETSEGMENTSOURCEINFO ns_GetSegmentSourceInfo;
extern NS_GETSEGMENTDATA       ns_GetSegmentData;
extern NS_GETNEURALINFO        ns_GetNeuralInfo;
extern NS_GETNEURALDATA        ns_GetNeuralData;
extern NS_GETINDEXBYTIME       ns_GetIndexByTime;
extern NS_GETTIMEBYINDEX       ns_GetTimeByIndex;
extern NS_GETLASTERRORMSG      ns_GetLastErrorMsg;
#endif


#ifdef __cplusplus
}
#endif



#endif          // end of include guards
